import numpy as np
import cv2
import logging
import json
from decimal import *


logger = logging.getLogger(__name__)


class ScaleDetection:
    def __init__(self):
        x_scale = None
        y_scale = None

    def calibrate(self, image, known_x, known_y):
        '''
        Given an image of an object of known size sets the x and y scale
        Args:
            image (string): file name of image
            known_x (float): length of the object in the horizontal dimension
            known_y (float): length of the object in the vertical dimension
        Returns:
            True on success, False on failure
        '''
        im = cv2.imread(image)
        try:
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        except cv2.error as e:
            print("Could not create gray image, ensure the given "
                  "filename exists")
            return False
        ret, thresh = cv2.threshold(imgray, 50, 255, 0)
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
        (w, h) = rectangle[1]  # dimensions in pixels
        # size in pixels is proportional to real scale
        # this scale times pixels can now determin scale
        # as long as the camera is kept at a fixed height

        try:
            self.x_scale = Decimal(known_x)/Decimal(w)
            self.y_scale = Decimal(known_y)/Decimal(h)
        except InvalidOperation:
            print "known_x and known_y must be numbers, retry calibration"
            return False
        return True

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
        self.x_scale = config["x_scale"]
        self.y_scale = config["y_scale"]

    def detectSize(self, image):
        '''
        For a calibrated system, detects the size of the largest object.
        Args:
            image: image file path
        Returns:
            A tuple of (width, height) of the rectangle bounding the
            object in real world units.
        '''
        if self.x_scale is None or self.y_scale is None:
            print "The system must be calibrated: x or y scale is still None"

        im = cv2.imread(image)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 50, 255, 0)
        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        max_contour = contours[max_index]

        # red box
        # rectangle contains (x, y), (w, h), theta (angle of rotation)
        rectangle = cv2.minAreaRect(max_contour)
        box = cv2.cv.BoxPoints(rectangle)
        box = np.int0(box)
        w, h = rectangle[1]
        width = Decimal(w) * Decimal(self.x_scale)
        height = Decimal(h) * Decimal(self.y_scale)
        return (width, height)
