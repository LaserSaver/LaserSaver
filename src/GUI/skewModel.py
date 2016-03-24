import time
import scanner
class SkewModel:
	def calculate(self, imgList):
		camSettings = Scanner.skewCalibration(imgList)

		#should return camSettings

		#For now return the last image in the list
		return imgList.pop()
