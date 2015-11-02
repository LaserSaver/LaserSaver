import numpy as np
import cv2
import logging
import json
from decimal import *


logger = logging.getLogger(__name__)
getcontext().prec = 50

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
        max_contour = contours[max_index]

        # rectangle contains (x,y), (w,h), theta (angle of rotation)
        rectangle = cv2.minAreaRect(max_contour)
        box = cv2.cv.BoxPoints(rectangle)
        box = np.int0(box)
        (w,h) = rectangle[1]  # dimensions in pixels
        # size in pixels is proportional to real scale
        # this scale times pixels can now determin scale
        # as long as the camera is kept at a fixed height

        self.x_scale = Decimal(known_x)/Decimal(w)
        self.y_scale = Decimal(known_y)/Decimal(h)

    def saveConfigFile(self, config_file="scale.config"):
        """
        saves a dictionary {"x_scale": self.x_scale, "y_scale": self.y_scale}
        Args:
            config_file: location of config file,
                       defaults to configs/scale.config.
        """
        data = {"x_scale": self.x_scale, "y_scale": self.y_scale}
        with open(config_file, 'w') as conf:
            json.dump(data, conf)


    def loadConfigFile(self, config_file="scale.config"):
        """
        Args:
            config_file: location of config file,
                       defaults to configs/scale.config.
        Returns:
            config: A dictionary of {"x_scale": val, "y_scale": val}

        """
        with open(config_file, 'r') as conf:
            config = json.load(conf)
        return config

    def detectSize(self, image):
        '''
        System must be calibrated.
        Args:
            image: image file path
        Returns:
            rectange: A tuple of (width, height) of the board in real world,
                    which is the largest contour
        '''
        if self.x_scale == None or self.y_scale == None:
            print "The system must be calibrated: x or y scale is still None"
        im = cv2.imread(image)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray, 50, 255, 0)
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
        w,h = rectangle[1]
        width = Decimal(w) * Decimal(self.x_scale)
        height = Decimal(h) * Decimal(self.y_scale)
        return (width, height)
