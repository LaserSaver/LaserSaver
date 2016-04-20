
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class ContoursModel:
    def __init__(self):
	    self.scanner = Scanner()

    def calculate(self, img):
        """
        Calls the scanner function to calculate contours and generate JSON
        Args:
            img: image to calculate contours on
        Returns:
            finalImage: image of the contours
        """
        finalImage = self.scanner.processImages(img)

        #Return stitched image, but doesn't have any contours on it currently
        return img
