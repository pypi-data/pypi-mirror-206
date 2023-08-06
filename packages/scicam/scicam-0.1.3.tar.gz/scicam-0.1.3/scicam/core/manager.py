import logging
import multiprocessing
import threading
import traceback
import queue

import pandas as pd
import yaml

from scicam.io.cameras import CAMERAS
from scicam.core.monitor import Monitor
from scicam.configuration import load_setup_cameras

logger = logging.getLogger(__name__)


class Manager:


    def __init__(
        self, idx, setup_name, supplier, camera_idx, format, output, sensor=None, roi_helper=None, select_roi=False,
        resolution_decrease=1.0, chunk_duration=300
    ):
        
        self.setup_name = setup_name
        self.supplier = supplier
        self.idx = idx
        self.camera_idx = camera_idx
        self.sensor = sensor
        self.roi_helper = roi_helper
        self.select_roi = select_roi
        self.root_output = output
        self.chunk_duration=chunk_duration
        self.format = format
        self.process = None
        self.stop_queue = None
        self.resolution_decrease=resolution_decrease


    @staticmethod
    def separate_process(
        setup_name,
        supplier,
        output,
        format,
        sensor=None,
        stop_queue=None,
        process_id=0,
        roi=None,
        camera_idx=0,
        start_time=None,
        chunk_duration=300,
        metadata={},
    ):
        logger.info("multiprocess.Process - scicam.bin.__main__.separate _process")

        logger.debug(f"Monitor running {setup_name} - {supplier} chunk_duration: {chunk_duration}")
        monitor = Monitor(
            setup_name=setup_name,
            supplier=supplier,
            path=output,
            format=format,
            start_time=start_time,
            stop_queue=stop_queue,
            sensor=sensor,
            roi=roi,
            select_roi=False,
            camera_idx=camera_idx,
            chunk_duration=chunk_duration,
            metadata=metadata,
        )


        logger.info(f"Monitor start time: {start_time}")

        monitor.process_id = process_id
        return monitor


    def init(
        self, start_time,
    ):
        config = load_setup_cameras(self.setup_name)[self.supplier]

        duration = config[self.camera_idx].get("duration", None)
        framerate = config[self.camera_idx]["framerate"]
        exposure = config[self.camera_idx]["exposure"]
        brightness = config[self.camera_idx]["brightness"]
        pixels_per_cm = config[self.camera_idx]["pixels_per_cm"]

        print(self.supplier, end=":")
        print(f"    Framerate {framerate}")
        print(f"    Exposure {exposure}")
        print(f"    Brightness {brightness}")

        if self.select_roi:

            camera = CAMERAS[self.supplier](
                start_time=start_time,
                roi_helper=self.roi_helper,
                resolution_decrease=self.resolution_decrease,
                exposure=exposure,
                brightness=brightness,
                camera_idx=self.camera_idx,
                apply_roi=False,
                # pixels_per_cm=pixels_per_cm,
            )

            logger.info(f"Selecting ROI for {camera}")
            if self.select_roi:
                roi = camera.select_ROI()
            # save the roi and somehow give it to the next instance
            camera.close()

        else:
            camera = CAMERAS[self.supplier](
                            start_time=start_time,
                            resolution_decrease=self.resolution_decrease,
                            camera_idx=self.camera_idx,
            )
            width=max(camera.width, camera.height)
            height=width
            camera.close()
            roi = (0, 0, width, height)
            
        self.stop_queue = queue.Queue(maxsize=1)       
        
        kwargs = {
            "setup_name": self.setup_name,
            "supplier": self.supplier,
            "output": self.root_output,
            "format": self.format,
            "sensor": self.sensor,
            "stop_queue": self.stop_queue,
            "process_id": self.idx,
            "roi": roi,
            # "hash": camera.__hash__(),
            "start_time": start_time,
            "chunk_duration": self.chunk_duration,
            # "min_bitrate": self._min_bitrate,
            # "max_bitrate": self._max_bitrate,
            "camera_idx": self.camera_idx,
            "metadata": {"pixels_per_cm": pixels_per_cm}
        }


        monitor=self.separate_process(
            **kwargs,
        )

        return monitor


    def start(self):
        return self.process.start()

    def join(self, *args, **kwargs):
        return self.process.join(*args, **kwargs)
    
    def is_alive(self, *args, **kwargs):
        return self.process.is_alive(*args, **kwargs)
