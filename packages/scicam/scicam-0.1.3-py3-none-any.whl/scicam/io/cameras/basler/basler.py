# Standard library
import logging
import time
import traceback
import os.path
import datetime

# Optional modules
from pypylon import pylon

# Local library
from scicam.io.cameras.core import CV2Compatible
from scicam.io.cameras.utils import ensure_img, validate_img
from scicam.decorators import timeit

logger = logging.getLogger("scicam.io.camera")
LEVELS = {"DEBUG": 0, "INFO": 10, "WARNING": 20, "ERROR": 30}

from scicam.configuration import load_setup_cameras 

class BaslerCamera(CV2Compatible):

    supplier="BaslerCamera"
    HEIGHT_STEPS=2
    WIDTH_STEPS=16

    """
    Drive a Basler camera using pypylon.
    """

    def __init__(self, *args, **kwargs):
        self._target_shape = None
        super(BaslerCamera, self).__init__(*args, **kwargs)

    @property
    def width(self):
        return self.camera.Width.GetValue()

    @property
    def height(self):
        return self.camera.Height.GetValue()

    @property
    def model_name(self):
        return self.camera.GetDeviceInfo().GetModelName()
    
    @property
    def serial_number(self):
        return self.camera.GetDeviceInfo().GetSerialNumber()


    @property
    def friendly_name(self):
        return self.camera.GetDeviceInfo().GetFriendlyName()

    @property
    def temperature(self):
        try:
            return round(self.camera.DeviceTemperature.GetValue(), 2)
        except Exception as error:
            print(error)
            return 0

    @property
    def temperature_unit(self):
        return self.camera.DeviceTemperature.GetUnit()


    @property
    def framerate(self):
        return float(self.camera.AcquisitionFrameRate.GetValue())

    @framerate.setter
    def framerate(self, framerate):
        logging.warning("Setting framerate is not recommended in scicam")
        self.camera.AcquisitionFrameRate.SetValue(framerate)
        self._target_framerate = framerate

    @property
    def exposure(self):
        return float(self.camera.ExposureTime.GetValue())

    @exposure.setter
    def exposure(self, exposure):
        logging.warning("Setting exposure time is not recommended in scicam")
        self.camera.ExposureTime.SetValue(exposure)
        self._target_exposure = exposure

    def is_open(self):
        """
        Return True if camera is opened
        """
        return self.camera.IsOpen()

    @timeit 
    def _next_image_default_timeit(self):
        if self.camera.IsGrabbing():
            with self._acquisition_lock:
                try:
                
                    try:
                        grab = self.camera.RetrieveResult(
                            self._timeout, pylon.TimeoutHandling_ThrowException
                        )
                        success=True
                    except Exception as error:
                        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Error detected {now}")
                        print(error)
                        print(traceback.print_exc())
                        success = False

                    try:
                        if success and grab.GrabSucceeded():
                            img = grab.GetArray()
                            if img is None:
                                code = 1
                                print("img is None")
                            else:
                                code = 0
                            grab.Release()
                        else:
                            img=None
                            code=1
                    except Exception as error:
                        print(error)
                        print(traceback.print_exc())
                        img = None
                        code = 1
                except KeyboardInterrupt:
                    print("Catch Ctrl-C")
                    return 2, None
            
            image_validation=validate_img(img, self._target_shape)
            if image_validation == 1:
                print(
                    f"frame fetched by {self} could not be validated.\n"
                    "look below what it looks like"
                )
                try:
                    print("img")
                    print("####")
                    print(img)
                except:
                    pass
                print("scicam trying to restore the camera...")
                code, img=ensure_img(self)
            elif image_validation == 2:
                return self._next_image_default_timeit()

            elif self._target_shape is None:
                self._target_shape = img.shape


            return code, img
        else:
            return 1, None

    def _next_image_default(self):
        (code, img), msec = self._next_image_default_timeit()
        if code == 2:
            self.close()
            return False, None
        else:
            logger.debug(f"Read image from {self.model_name} in {msec} ms")
            status = 1 - code
            return status, img

    def _init_camera(self):
        
        # NOTE
        # When selecting a particular camera
        # you may want to use self.idx

        try:
            tl_factory = pylon.TlFactory.GetInstance()
            camera_device = tl_factory.CreateFirstDevice()
            self.camera = pylon.InstantCamera(
                camera_device
            )
        except Exception as error:
            logger.error(
                "The Basler camera cannot be opened."\
                " Please check error trace for more info"
            )
            logger.error(traceback.print_exc())
            raise error

    def _init_multi_camera(self, idx=0, timeout=None):

        try:
            tl_factory = pylon.TlFactory.GetInstance()
            devices = tl_factory.EnumerateDevices()
            waiting_time = 0
            while len(devices) == 0:
                if timeout is not None and waiting_time > timeout:
                    raise Exception(f"Timeout ({timeout}) reached. Scicam cannot find more devices")

                print("No devices left. Trying again in 1 second ...")
                time.sleep(1)
                waiting_time += 1
                devices = tl_factory.EnumerateDevices()
                # TODO Select devices not by position in devices list,
                # but by another attribute that is really unmistakingly
                # pointing to the righ camera
            print(f"Found {len(devices)} devices after {waiting_time} seconds!")
            device=None
            for a_device in devices:
                serial_number = int(a_device.GetSerialNumber())

                if serial_number == idx:
                    device = a_device
            if device is None:
                raise Exception(f"Basler camera with id {idx} not found")

            self.camera = pylon.InstantCamera(tl_factory.CreateDevice(device))
            self._idx = idx
            return 0

        except Exception as error:
            logger.error(
                "The Basler camera cannot be opened."\
                " Please check error trace for more info"
            )
            logger.error(traceback.print_exc())
            raise error
    

    def _compute_final_framerate_for_camera(self):
        """
        Add to the target framerate a little bit more,
        so the camera makes a bit more effort and actually hits the target
        """
        framerate = self._target_framerate + self._framerate_offset
        max_framerate = self.camera.AcquisitionFrameRate.GetMax()
        if framerate >= max_framerate:
            logger.warning(
                f"Passed framerate is greater or equal than max ({max_framerate})"
            )
            final_framerate = max_framerate
        else:
            final_framerate = framerate
        return final_framerate

    def save_features(self, pfs_file):
        assert self.is_open()
        return pylon.FeaturePersistence.Save(pfs_file, self.camera.GetNodeMap())
    
    
    @property
    def WidthMax(self):
        return self.camera.WidthMax.GetValue()
    
    @property
    def HeightMax(self):
        return self.camera.HeightMax.GetValue()


    def open(self, maxframes=None, buffersize=5, idx=0, apply_roi=True):
        """
        Detect a Basler camera using pylon
        Assign it to the camera slot and try to open it
        Try to fetch a frame
        """
        self._init_multi_camera(idx=idx)
        print(f"Opening camera with index {idx}")
        self.camera.Open()
        print("Using device ", self.model_name)
        config=load_setup_cameras()["BaslerCamera"]

        if apply_roi:
            for key in ["Width", "Height", "OffsetX", "OffsetY"]:
                value = config[idx].get(key, None)
                if value is not None:
                    getattr(self.camera, key).SetValue(value)
                    print(f"Setting {key} = {value}")

        else:
            self.camera.OffsetX.SetValue(0)
            self.camera.OffsetY.SetValue(0)
            self.camera.Width.SetValue(self.WidthMax)
            self.camera.Height.SetValue(self.HeightMax)
            

        self.camera.AcquisitionFrameRateEnable.SetValue(True)

        final_framerate=self._compute_final_framerate_for_camera()
        logger.debug(f"{self} setting framerate to {final_framerate}")
        self.camera.AcquisitionFrameRate.SetValue(
            final_framerate
        )
        logger.debug(f"{self} setting exposure to {self._target_exposure}")
        self.camera.ExposureTime.SetValue(self._target_exposure)
        self.camera.ReverseX.SetValue(False)
        self.camera.ReverseY.SetValue(False)
        self.camera.MaxNumBuffer = buffersize
        
        if self._document_path is not None:
            self.save_features(
                os.path.join(
                    self._document_path,
                    self.model_name + ".pfs"
                )
            )

        if maxframes is not None:
            self.camera.StartGrabbingMax(maxframes)
            # if we want to limit the number of frames
        else:
            self.camera.StartGrabbing(pylon.GrabStrategy_OneByOne)

        # Print the model name of the camera.
        logger.info(f"Using device {self.model_name}")
        self._init_read()

    def close(self):
        print("Waiting for acquisition lock")
        while self._acquisition_lock.locked():
            time.sleep(.1)

        print(f"Closing camera {self.friendly_name}")
        with self._acquisition_lock:
            self.camera.Close()
