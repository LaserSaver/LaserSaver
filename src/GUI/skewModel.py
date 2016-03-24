import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scanner
class SkewModel:
	def calculate(self, imgList):
		camSettings = Scanner.skewCalibration(imgList)

		#should return camSettings

		#For now return the last image in the list
		return imgList.pop()
