import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class SkewModel:
    def __init__(self):
	    self.scanner = Scanner()
    
    def calculate(self, imgList):
        """
        calibrates the scale and saves to config file
        Args:
            scaleDetect (ScaleDetection):
            image: the calibration image
            objx: width of calibration object
            objy: height of calibration object
            units (string): units to use
        Returns:
            True on success, False on failure
        """
        try:
            self.scanner.skewCalibration(imgList,1)
        except AttributeError:
            print "No going"
            
        return imgList[0]