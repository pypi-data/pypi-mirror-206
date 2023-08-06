import cv2
from sklearn.metrics import RocCurveDisplay
import numpy as np
from cv2cuda.decorator import timeit
import functools
from scicam.configuration import load_setup_cameras, save_setup_cameras

def make_square(easy_roi_circle):

    x = easy_roi_circle["center"][0] - easy_roi_circle["radius"]
    y = easy_roi_circle["center"][1] - easy_roi_circle["radius"]
    h = w = easy_roi_circle["radius"] * 2
    return [x, y, w, h]

    
class ROIPlugin:
    _ROIbackend = "EasyROI"

    """
    
    Needed signatures

    status, image = self._next_image_square()
    width, height = self.resolution   
    """

    def __init__(self,  *args, roi_helper=None, **kwargs):
        self._roi_helper = roi_helper
        super(ROIPlugin, self).__init__(*args, **kwargs)


    @staticmethod
    def _crop_roi(image, roi):
        return image[
            int(roi[1]) : int(roi[1] + roi[3]),
            int(roi[0]) : int(roi[0] + roi[2]),
        ]


    @staticmethod
    def _process_roi(r, fx, fy):
        r[0] = int(r[0] * fx)
        r[1] = int(r[1] * fy)
        r[2] = int(r[2] * fx)
        r[3] = int(r[3] * fy)
        roi = tuple(r)
        return roi

    def _select_roi(self, image):

        if self._roi_helper and self._ROIbackend == "EasyROI":
            while True:
                roi = self._roi_helper.draw_circle(image, quantity=1)["roi"][0]
                print("circle: ", roi)
                roi = make_square(roi)
                print("square: ", roi)

                mask = np.zeros_like(image)
                mask[
                    roi[1]:(roi[1] + roi[3]),
                    roi[0]:(roi[0] + roi[2]),
                ] = 255
                applied = cv2.bitwise_and(image, mask)
                cv2.imshow("Selected", applied)
                if cv2.waitKey(0) == 32: #spacebar
                    break

       
        elif self._ROIbackend == "cv2":
            raise NotImplementedError()
            roi = cv2.selectROI("select the area", image)
                
        while any([v < 0 for v in roi]):
            roi = self._select_roi(image)
        
        return roi


    def select_ROI(self):
        """
        Select 1 ROI
        """
        status, image = self._next_image_default()
        
        if image.shape[0] > 1500:
            factor = 8
        else:
            factor = 4
        
        fy = fx = factor
        width = int(image.shape[1] / fx)
        height = int(image.shape[0] / fy)
        
        image=cv2.resize(image, (width, height))
        roi = self._select_roi(image)
        cv2.destroyAllWindows()

        roi = self._process_roi(roi, fx, fy)
        print("Selected ROI: ", roi)

        x = roi[0]
        
        if x % factor != 0:
            x -= x%factor
        
        y = roi[1]
        
        w = roi[2]
        h = roi[3]
        
        height_excess = w % self.HEIGHT_STEPS
        if height_excess != 0:
            h -= height_excess
        
        width_excess = w % self.WIDTH_STEPS
        if width_excess != 0:
            w -= width_excess
            
        if x % 2 !=0:
            x-=1
        
        if y % 2 != 0:
            y -=1

        # if h + y > self.HeightMax:
        #     y = self.HeightMax - h
        
        # if w + x > self.WidthMax:
        #     x = self.WidthMax - w

        roi = (x, y, w, h)
        self.save_roi(roi)
        self._roi = roi

        return (0, 0, w, h)

    def save_roi(self, roi):
        config = load_setup_cameras()
        x, y, w, h = roi
        
        config[self.supplier][self.camera_idx]["Width"] = w
        config[self.supplier][self.camera_idx]["Height"] = h
        config[self.supplier][self.camera_idx]["OffsetX"] = x
        config[self.supplier][self.camera_idx]["OffsetY"] = y        
        res=save_setup_cameras(config)
        
        config = load_setup_cameras()
        assert "pixels_per_cm" in config[self.supplier][self.camera_idx]
        
        return res
        

    @property
    def roi(self):
        if self._roi is None:
            try:
                return [(0, 0, *self.resolution)]
            except:
                raise Exception(
                    "Please open the camera before asking for its resolution"
                )
        else:
            return self._roi



class CameraUtils:

    def _count_frames_in_second(self):
        offset = self._time_s % 1000
        if offset < self._last_offset:
            self._last_offset = offset
            self._frames_this_second = 0
        else:
            self._frames_this_second += 1

class SquareCamera:

    VALUE_OF_BACKGROUND=255

    @staticmethod
    @functools.lru_cache
    def _compute_pad(shape):

        if shape[1] > shape[0]:
            left = right = 0
            bottom = top = (shape[1] - shape[0]) / 2
            diff = shape[1] - shape[0] - bottom - top
            if diff > 0:
                bottom += diff
        
        elif shape[0] > shape[1]:
            top = bottom = 0
            left = right = (shape[0] - shape[1]) / 2
            diff = shape[0] - shape[1] - left - right
            if diff > 0:
                right += diff
        
        else:
            top = bottom = left = right = 0

        
        return int(top), int(bottom), int(left), int(right)

    @timeit
    def apply_pad(self, image):
        top, bottom, left, right = self._compute_pad(image.shape)
        image = cv2.copyMakeBorder(image,
            top, bottom, left, right,
            borderType=cv2.BORDER_CONSTANT, value=self.VALUE_OF_BACKGROUND
        )
        return image

    def _next_image_square(self):
        code, image = self._next_image_default()

        if image is not None:
            if image.shape[0] != image.shape[1]:
                image, msec = self.apply_pad(image)
                assert image.shape[0] == image.shape[1]

        # print(image.shape)
        return code, image
