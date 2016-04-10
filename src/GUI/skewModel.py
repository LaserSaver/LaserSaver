import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner
class SkewModel:
    def __init__(self):
	    self.scanner = Scanner()
    
    def calculate(self, imgList):
        try:
            self.scanner.skewCalibration(imgList)
        except AttributeError:
            print "No going"
            
        return imgList.pop()
