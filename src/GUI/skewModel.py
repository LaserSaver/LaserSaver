import time
import sys
import os
import cv2
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class SkewModel:
    def __init__(self):
	    self.scanner = Scanner()

    def calculate(self, imgList):
        """
        Calls the scanner function to calculate skew correction values
        Args:
            imgList: Array of images used for calibration
        Returns:
            imgList[0]: First image taken
        """
        returnImage = self.scanner.skewCalibration(imgList,1)
        # try:
#             returnImage = self.scanner.skewCalibration(imgList,1)
#         except AttributeError:
#             print "No going"

        returnImage = cv2.imread("corrected.jpg")
        return returnImage
