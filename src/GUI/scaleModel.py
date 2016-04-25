import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class ScaleModel:
    def __init__(self):
        self.scanner = Scanner()

    def calculate(self, img, width, height, units):
        """
        Calls the scanner function to calculate scale
        Args:
            img: the calibration image
            width: width of calibration object
            height: height of calibration object
            units (string): units to use
        Returns:
            True on success, False on failure
        """
        scaleDetectObj = self.scanner.scaleCalibration(img, width, height, units)

        #should return scaleDetectObj

        #Return true for wentWell for now

        return True
