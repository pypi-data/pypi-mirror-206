import logging
import os.path
import time
import math

logger = logging.getLogger(__name__)
write_logger = logging.getLogger("scicam.write_logger")

import multiprocessing
import threading
import queue
import pandas as pd
import arrayqueues
from scicam.io.recorders import ImgStoreRecorder
from scicam.web_utils.sensor import setup as setup_sensor
from scicam.exceptions import ServiceExit
from scicam.io.cameras import CAMERAS
from scicam.utils import load_config
import psutil
from scicam.configuration import load_setup_cameras

class Monitor(threading.Thread):
    _RecorderClass = ImgStoreRecorder

    def __init__(
        self,
        setup_name,
        supplier,
        path,
        format,
        start_time,
        *args,
        stop_queue=None,
        sensor=None,
        roi=None,
        select_roi=False,
        chunk_duration=300,
        camera_idx=0,
        metadata={},
    ):

        self.supplier = supplier
        self._root_path = path
        self._select_roi = select_roi
        self._camera_idx = camera_idx
        os.makedirs(self._root_path, exist_ok=True)
        logger.debug(f"{self} chunk_duration: {chunk_duration}")

        self._process = psutil.Process(os.getpid())

        self.setup_camera(
            setup_name=setup_name,
            camera_idx=camera_idx,
            supplier=supplier,
            roi=roi,
            start_time=start_time,
        )

        self._stop_queue = stop_queue
        self._setup_queues()
        self._stop_event = multiprocessing.Event()

        self._recorder = None

        metadata.update({
            "camera-framerate": self.camera.framerate,
            "camera-exposure": self.camera.exposure,
            "camera-model": self.camera.model_name,
        })

        self._recorder= self._RecorderClass(
            framerate=float(int(self.camera.framerate)),
            duration=self.camera.duration,
            resolution = self.camera.roi[2:4],
            path=self._root_path,
            data_queue = self._data_queue,
            stop_queue = self._stop_queue,
            sensor=sensor,
            idx=0,
            roi=self.camera.roi,
            format=format,
            chunk_duration=chunk_duration,
            metadata=metadata,
        )
        super(Monitor, self).__init__()


    def __str__(self):
        return f"Monitor driving camera {self.supplier} - {self._camera_idx}"


    def _setup_queues(self):

        self._data_queue = arrayqueues.TimestampedArrayQueue(5000) # 5gb buffer
        self._stop_queue =multiprocessing.Queue(maxsize=1)

    def setup_camera(self, setup_name, supplier, camera_idx, **kwargs):
        config = load_setup_cameras(setup_name)[supplier]

        # duration = config[camera_name]["duration"]
        framerate = config[camera_idx]["framerate"]
        exposure = config[camera_idx]["exposure"]
        brightness = config[camera_idx]["brightness"]

        print(supplier, end=":")
        print(f"    Camera idx {camera_idx}")
        print(f"    Framerate {framerate}")
        print(f"    Exposure {exposure}")
        print(f"    Brightness {brightness}")


        self.camera = CAMERAS[supplier](
            document_path=self._root_path,
            framerate=framerate,
            exposure=exposure,
            brightness=brightness,
            duration=None,
            camera_idx=camera_idx,
            **kwargs
        )

        if self._select_roi:
            self.camera.select_ROI()

    def open(self):

        recorder_path = f"{self._root_path.rstrip('/')}_ROI_0"
        self._recorder.open(
            path=recorder_path
        )
        logger.info(
            f"{self._recorder} for {self.camera} has recorder_path = {recorder_path}"
        )

    def put(self, recorder, data_queue, data):

        timestamp, i, arr, info = data
        try:
            data_queue.put(arr, timestamp=(timestamp, i, info))
            recorder._n_saved_frames += 1
        except queue.Full:
            # data_queue.get()
            recorder.n_lost_frames += 1
            if recorder.n_lost_frames % 100 == 0 or recorder.n_saved_frames % 100 == 0:
                logger.warning(
                    f"{self} Data queue is full!"\
                    f" Wrote {recorder.n_saved_frames} frames."\
                    f" Lost {recorder.n_lost_frames} frames"\
                    f" That means ({100 * recorder.n_lost_frames / recorder.n_saved_frames}) % of all frames are dropped"
                )


    def run(self):

        logger.info("Monitor starting")
        self._start_time = self.camera.start_time

        self._recorder.start_time = self._start_time
        self._recorder.start()
        logger.debug("Recorder starting")

        last_timestamp = 0
        input("Continue?")

        for frame_idx, (timestamp, frame, info) in enumerate(self.camera):
            # proc_time = timestamp - last_timestamp
            # logger.debug(
            #     f"Frame processing time: {proc_time}"
            #     f"FPS approx {round(1000/proc_time, 2)}"
            # )
            if frame_idx % (int(self.camera.framerate) * 60) == 0:
                print(self.camera, self._process.memory_info().rss / (1024)**2)

            if self._stop_event.is_set():
                logger.info("Monitor exiting")

                logger.debug(
                    f"Recorder 0 output queue has {self._recorder.buffer_usage} frames"
                )
                break

            if self._stop_queue is not None:
                try:
                    msg = self._stop_queue.get(False)
                except queue.Empty:
                    msg = None
                if msg == "STOP":
                    logger.debug(f"Setting {self} stop event")
                    self._stop_event.set()

            self.put(
                recorder=self._recorder,
                data_queue=self._data_queue,
                data=(timestamp, frame_idx, frame, info)
            )
            # _, write_msec = recorder.write(timestamp, frame_idx, frame[i])
            # write_logger.debug(f"Recorder took {write_msec} ms to write")
            last_timestamp = timestamp

        logger.debug("Joining recorders")
        recorder = self._recorder
        if recorder.is_alive():
            while not recorder.all_queues_have_been_emptied:
                time.sleep(1)
                logger.debug("Waiting for", recorder)

            logger.debug("Report one last time ", recorder)
            recorder.check_data_queue()
            logger.debug("Close tqdm for ", recorder)
            logger.debug("Joining", recorder)
            # recorder._data_queue.put(None)
        recorder.join()
        logger.debug("JOOOOIIIIIINEEEEDD")

        logger.debug("Joined all recorders")

    def close(self):

        # this makes the run method exit
        # because it checks if the stop_event is set
        self._stop_event.set()
        logger.info("Monitor closing")
        self._recorder.close()


def run(monitor):

    monitor.open()
    try:
        monitor.start()
        time.sleep(5)
        monitor.join()
        # while monitor.is_alive():
        #    print("Running time sleep forever")
        #    time.sleep(0.5)

    except ServiceExit:
        print("ServiceExit captured at Monitor level")
        monitor.close()
    except Exception as error:
        print(error)
    finally:
        print(f"Joining monitor {monitor}")
        monitor.join()
        print(f"Joined monitor {monitor}")
        if monitor._stop_queue is not None:
            print(f"stop_queue size: {monitor._stop_queue.qsize()}")

        for some_queue in monitor._stop_queues:
            print(f"{some_queue} size: {some_queue.qsize()}")


