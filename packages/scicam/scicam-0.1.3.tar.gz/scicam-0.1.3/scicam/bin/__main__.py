import argparse
import sys
import time
import os.path
import signal

import numpy as np
import yaml
from datetime import datetime
import logging
import logging.config
from scicam.constants import LOGGING_CONFIG
from EasyROI import EasyROI

from scicam.io.cameras.__main__ import get_parser as flir_parser
from scicam.io.cameras.basler.parser import get_parser as basler_parser
from scicam.io.cameras import CAMERAS
from scicam.io.recorders.parser import get_parser as recorder_parser
from scicam.web_utils.sensor import setup as setup_sensor
from scicam.core.manager import Manager
from scicam.exceptions import ServiceExit
from scicam.utils import load_config, service_shutdown
from scicam.configuration import load_setup_cameras

logger = logging.getLogger(__name__)

config = load_config()
ROOT_OUTPUT=config["videos"]["folder"]
LOGFOLDER=config["logs"]["folder"]

# this start time will be shared by all cameras running in parallel and will give name to the experiment


with open(LOGGING_CONFIG, 'r') as filehandle:
    logging_config = yaml.load(filehandle, yaml.SafeLoader)
    logging.config.dictConfig(logging_config)



def get_parser(ap=None):

    if ap is None:
        ap = argparse.ArgumentParser(conflict_handler="resolve")

    ap.add_argument(
        "--start-time",
        required=True,
        type=int,
        help='Timestamp in seconds as produced by date +"%s" in Linux or time.time() in Python'
        )

    ap.add_argument(
        "--supplier",
        type=str,
        required=False,
    )
    ap.add_argument(
        "--setup",
        type=str,
        required=False,
    )
    ap.add_argument("--X", type=int, required=True)

    ap.add_argument(
        "--sensor",
        type=int,
        default=9000,
        help="Port of environmental sensor",
    )
    ap.add_argument(
        "--select-roi",
        default=False,
        action="store_true",
        dest="select_roi",
        help="""
        Whether a region of interest (ROI)
        of the input should be cropped or not.
        In that case, a pop up will show for the user to select it
        """,
    )

    return ap


def get_queue(process, queues):
    if process in queues and not queues[process].empty():
        timestamp, frame = queues[process].get()
        return timestamp, frame
    else:
        return (None, np.uint8())


def setup_and_run(args):
    sensor = setup_sensor(args.sensor)
    managers = {}

    if args.select_roi:
        roi_helper = EasyROI(verbose=True)
    else:
        roi_helper = None


    monitors=[]

    start_time = args.start_time
    time_iso_8601=datetime.fromtimestamp(start_time).strftime("%Y-%m-%d_%H-%M-%S")
    LOGFILE = os.path.join(config["logs"]["folder"], f"{time_iso_8601}.log")
    file_handler = logging.FileHandler(LOGFILE, mode='w')

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)


    suppliers = load_setup_cameras()


    if args.setup is not None:
        new_suppliers={}
        for supplier in suppliers:
            new_suppliers[supplier] ={}

        for supplier in suppliers:
            for camera in suppliers[supplier]:
                if suppliers[supplier][camera]["setup"] == args.setup:
                    new_suppliers[supplier][camera] = suppliers[supplier][camera]

        suppliers = new_suppliers

    if args.supplier is not None:
        suppliers = {args.supplier: suppliers[args.supplier]}


    for i, supplier in enumerate(suppliers):
        cameras = suppliers[supplier]
        for camera_idx in cameras:
            role = cameras[camera_idx]["role"]
            setup_name = cameras[camera_idx]["setup"]
            camera_name = supplier
            root_output = os.path.join(ROOT_OUTPUT, setup_name, f"{args.X}X", time_iso_8601)
            os.makedirs(root_output, exist_ok=False)
            LOGFILE = os.path.join(LOGFOLDER, setup_name, f"{time_iso_8601}.log")
            os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
            file_handler = logging.FileHandler(LOGFILE, mode='w')
            logger.addHandler(file_handler)


            if role == "highspeed":
                output = os.path.join(root_output, role)
            else:
                output = root_output

            # if supplier == "FlirCamera":
            #     encoder_kwargs = {"gop_duration": 60}
            # else:
            #     encoder_kwargs = {}

            manager = Manager(
                idx=i,
                chunk_duration=args.chunk_duration,
                setup_name=setup_name, supplier=camera_name, camera_idx=camera_idx, output=output, format=args.format,
                sensor=sensor,  select_roi=args.select_roi, roi_helper=roi_helper
            )
            managers[camera_name] = manager
            # kwargs = manager.init(start_time)
            monitors.append(manager.init(start_time))#, encoder_kwargs=encoder_kwargs))

    for monitor in monitors:
        monitor.start()

    for monitor in monitors:
        monitor.join()


    try:
        logger.debug(f"Starting {len(managers)} processes")
        run_processes(managers)
    except KeyboardInterrupt:
        return


def run_processes(managers):

    if "FlirCamera" in managers:
        managers["FlirCamera"].start()
    # give time for the Flir process to start
    # before Basler does.
    # Otherwise Basler starts before and crashes when Flir does

    if "FlirCamera" in managers and "BaslerCamera" in managers:
        time.sleep(5)
    if "BaslerCamera" in managers:
        managers["BaslerCamera"].start()
    time.sleep(1)

    try:
        for p in managers.values():
            p.join()
    except ServiceExit:
        print(
            """
          Service Exit captured.
          Please wait until processes finish
        """
        )
        for manager in managers.values():
            manager.stop_queue.put("STOP")

        for m in managers.values():
            m.join()
        sys.exit(0)

    if all([not p.is_alive() for p in managers.values()]):
        sys.exit(0)


def main(args=None, ap=None):

    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)

    if args is None:
        if ap is None:
            ap = get_parser()
            ap = basler_parser(ap=ap)
            ap = flir_parser(ap=ap)
            ap = recorder_parser(ap)
        args = ap.parse_args()

    setup_and_run(args)


if __name__ == "__main__":
    main()
