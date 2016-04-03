import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner
class SkewModel:

	def __init__(self):
		self.scanner = Scanner()

	def calculate(self, imgList):
		camSettings = self.scanner.skewCalibration(imgList)

		#should return camSettings

		#For now return the last image in the list
		return imgList.pop()
