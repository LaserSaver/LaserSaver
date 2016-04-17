import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class ScaleModel:
    def __init__(self):
        self.scanner = Scanner()
        
    def calculate(self, img, width, height, units):
        #scaleDetectObj = self.scanner.scaleCalibration(img, width, height, units)
        
        #should return scaleDetectObj
        
        #Return true for wentWell for now
        
        return True