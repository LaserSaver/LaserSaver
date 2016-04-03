import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scanner
class ScaleModel:
	def calculate(self, img1, img2, width, height, units):
		scaleDetectObj = Scanner.scaleCalibration(img1, img2, width, height, units)

		#should return scaleDetectObj

		#Return true for wentWell for now
		return True