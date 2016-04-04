import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner
class ContoursModel:
    def __init__(self):
	    self.scanner = Scanner()
    
    def calculate(self, img, img2):
        finalImage = self.scanner.processImages(img, img2)
        
        #Return stitched image, but doesn't have any contours on it currently
        return finalImage
