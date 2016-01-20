import numpy as np
import cv2
import logging
import json
from decimal import *


logger = logging.getLogger(__name__)


class ScaleDetection:
    '''
    ScaleDetection objects translate between pixals and real world dimensions.
    '''
    def __init__(self):
        '''
        Initialize a new ScaleDetection object
        '''
        x_scale = None
        y_scale = None

    def getScale(self):
        '''
        Returns tuple of (self.x_scale, self.y_scale)
        '''
        return (self.x_scale, self.y_scale)

    def calibrate(self, image, known_x, known_y, show_conts=False):
        '''
        Given an image of an object of known size sets the x and y scale
        Args:
            image (string): file name of image
            known_x (number): length of the object in the horizontal dimension
            known_y (number): length of the object in the vertical dimension
        Returns:
            True on success, False on failure
        '''
        im = cv2.imread(image)
        try:
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # object will be black and background will be white
            # we need the opposite
            imgray = (255-imgray)
        except cv2.error as e:
            print("Could not create gray image, ensure the given "
                  "filename exists")
            return False

        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
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
        # logger.DEBUG("(w, h): ({}, {})".format(w, h))
        print("(w, h): ({}, {})".format(w, h))

        # size in pixels is proportional to real scale
        # this scale times pixels can now determin scale
        # as long as the camera is kept at a fixed height

        try:
            self.x_scale = Decimal(known_x)/Decimal(w)
            self.y_scale = Decimal(known_y)/Decimal(h)
        except InvalidOperation:
            print "known_x and known_y must be numbers, retry calibration"
            return False
        print("(x_scl, y_scl): ({}, {})".format(self.x_scale, self.y_scale))

        if show_conts:
            cv2.drawContours(im, [box], 0, (0,0,255), 2)
            cv2.imwrite(image+'_rec', im)
        return True



    def saveConfigFile(self, config_file="scale.config"):
        """
        saves a dictionary {"x_scale": self.x_scale, "y_scale": self.y_scale}
        Args:
            config_file (string): location of config file,
                       defaults to configs/scale.config.
        Returns:
            True on success, False on failure
        """
        data = {"x_scale": self.x_scale, "y_scale": self.y_scale}
        with open(config_file, 'w') as conf:
            json.dump(data, conf)
        return True

    def loadConfigFile(self, config_file="scale.config"):
        """
        Loads the x and y scale from the config file.
        Args:
            config_file (string): location of config file,
                       defaults to configs/scale.config.
        Returns:
            True on success, False on failure
        """
        try:
            with open(config_file, 'r') as conf:
                config = json.load(conf)
        except IOError as e:
            print(e)
            return False
        self.x_scale = config["x_scale"]
        self.y_scale = config["y_scale"]
        return True

    def detectSize(self, image, show_conts=False):
        '''
        For a calibrated system, detects the size of the largest object.
        Args:
            image (string): image file path
        Returns:
            A tuple of (width, height) of the rectangle bounding the
            object in real world units. Returns (None, None) if
            unsuccessful.
        '''
        if self.x_scale is None or self.y_scale is None:
            print "The system must be calibrated: x or y scale is still None"
            return (None, None)

        im = cv2.imread(image)
        try:
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            imgray = (255-imgray)
        except cv2.error as e:
            print("Could not create gray image, ensure the given "
                  "filename exists")
            return False
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
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
        if show_conts:
            cv2.drawContours(im, [box], 0, (0,0,255), 2)
            cv2.imwrite(image+'_rec', im)
        h, w = rectangle[1]
        print w
        print h
        width = Decimal(w) * Decimal(self.x_scale)
        height = Decimal(h) * Decimal(self.y_scale)
        cv2.drawContours(im, [box], 0, (0,0,255),2)
        cv2.imwrite(image+"_rec", im)
        return (width, height)
