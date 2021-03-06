import numpy as np
import cv2
import logging
import json
import time
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
        units = None

    def getScale(self):
        '''
        Returns tuple of (self.x_scale, self.y_scale)
        '''
        return (self.x_scale, self.y_scale, self.units)
        
    def setScale(self, x_scale, y_scale, units):
        
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.units = units


    def openImage(self, filename):
        '''
        Given the filename of an image, returns the image object
        Args:
            filename (string): filename of image
        Returns:
            cv2 image object, None on failure
        '''
        try:
            image = cv2.imread(filename)
        except:
            image = None
        return image

    def calibrate(self, image, known_x, known_y, unit, show_conts=False):
        '''
        Given an image of an object of known size sets the x and y scale
        Args:
            image (string): file name of image
            known_x (number): length of the object in the horizontal dimension
            known_y (number): length of the object in the vertical dimension
            show_conts(optional[bool]): if True an image with the object
                selected in red will be saved as image_rec
        Returns:
            True on success, False on failure
        '''
        (w, h) = self.getDimensions(image, show_conts=show_conts)
        if w is None or h is None :
            print "width or height is None"
            return False
        if float(w) is 0 or float(h) is 0:
            print "width or height is 0"
            return False

        # size in pixels is proportional to real scale
        # this scale times pixels can now determin scale
        # as long as the camera is kept at a fixed height
        try:
            self.x_scale = Decimal(known_x)/Decimal(w)
            self.y_scale = Decimal(known_y)/Decimal(h)
        except InvalidOperation:
            print "known_x and known_y must be numbers, retry calibration"
            return False
        self.units = unit
        logger.debug("(x_scl, y_scl, units): ({}, {}, {})".format(self.x_scale,
                                                                  self.y_scale,
                                                                  self.units))
        return True



    def saveConfigFile(self, config_file="scale.config"):
        """
        saves a dictionary {"x_scale": self.x_scale,
                            "y_scale": self.y_scale,
                            "units": self.units}
        Args:
            config_file (string): location of config file,
                       defaults to configs/scale.config.
        Returns:
            True on success, False on failure
        """
        data = {"x_scale": self.x_scale,
                "y_scale": self.y_scale,
                "units": self.units}

        # with open(config_file, 'w') as conf:
        #     json.dump(data, conf)

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
        except ValueError:
            return False
        self.x_scale = config["x_scale"]
        self.y_scale = config["y_scale"]
        self.units = config["units"]
        return True


    def getSize(self, image, show_conts=False):
        '''
        For a calibrated system, detects the size of the largest object.
        Args:
            image (string): image file path
            show_conts(optional[bool]): if True an image with the object
                selected in red will be saved as image_rec
        Returns:
            A tuple of (width, height) of the rectangle bounding the
            object in real world units. Returns (None, None) if
            unsuccessful.
        '''
        if self.x_scale is None or self.y_scale is None:
            print "The system must be calibrated: x or y scale is still None"
            return (None, None)

        (w, h) = self.getDimensions(image, show_conts=show_conts)
        width = Decimal(w) * Decimal(self.x_scale)
        height = Decimal(h) * Decimal(self.y_scale)
        return (width, height, self.units)


    def getDimensions(self, image, show_conts=False):
        '''
        Detects the size of the largest object.
        Args:
            image (string): image file path
            show_conts(optional[bool]): if True an image with the object
                selected in red will be saved as image_rec
        Returns:
            A tuple of (w, h) of the rectangle bounding the
            object in pixels. Returns (None, None) if
            unsuccessful.
        '''
        im = image
        try:
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # object will be black and background will be white
            # we need the opposite
            # imgray = (255-imgray)
        except:
            print("Could not create gray image, ensure the given "
                  "filename exists")
            return (None, None)

        # thresh is the binary image
        ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

        _, contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        max_contour = contours[max_index]

        # red box
        # rectangle contains (x, y), (h, w), theta (angle of rotation)
        rectangle = cv2.minAreaRect(max_contour)
        box = cv2.boxPoints(rectangle)
        box = np.int0(box)

        # green box
        # x,y,w,h = cv2.boundingRect(max_contour)
        # cv2.rectangle(im, (x,y), (x+w, y+h), (0, 255, 0), 2)

        if show_conts:
            cv2.drawContours(im, [box], 0, (0,0,255), 2)
            cv2.imwrite(str(time.time())+".jpg", im)
        h, w = rectangle[1]
        logger.debug("h: {}, w: {}".format(h, w))
        # print"h: {}, w: {}".format(h, w)
        return (w, h)
