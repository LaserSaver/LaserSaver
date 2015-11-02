import numpy as np
import cv2
import logging


logger = logging.getLogger(__name__)


class ScaleDetection:
    def __init__(self):
        x_scale = None
        y_scale = None

    def calibrate(self, image, known_x, known_y):
        im = cv2.imread(image)

        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,50,255,0)
        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        max_countour = contours[max_index]

        # rectangle contains (x,y), (w,h), theta (angle of rotation)
        rectangle = cv2.minAreaRect(cnt)
        box = cv2.cv.BoxPoints(rectangle)
        box = np.int0(box)
        (w,h) = rectangle[1]  # dimensions in pixels

        # size in pixels is proportional to real scale
        # this scale times pixels can now determin scale
        # as long as the camera is kept at a fixed height
        self.x_scale = x/w
        self.vert_scale = y/h

    def saveConfigFile(self, config="scale.config"):
        pass

    def loadConfigFile(
        pass

    def detectSize(self, image):
        '''
        For a calibrated system, given an image detectSize returns
        (width, height) of the board (which is the largest contour)
        '''
        im = cv2.imread(image)

        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,50,255,0)
        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        max_contour=contours[max_index]

        # red box
        # rectangle contains (x,y), (w,h), theta (angle of rotation)
        rectangle = cv2.minAreaRect(max_contour)
        box = cv2.cv.BoxPoints(rectangle)
        box = np.int0(box)
        return rectangle[1]
