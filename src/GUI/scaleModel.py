import time
import scanner
class ScaleModel:
	def calculate(self, img1, img2, width, height, units):
		scaleDetectObj = Scanner.scaleCalibration(img1, img2, width, height, units)

		#should return scaleDetectObj

		#Return true for wentWell for now
		return True