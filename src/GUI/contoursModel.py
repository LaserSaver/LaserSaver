import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scanner
class ContoursModel:
	def calculate(self, img, img2, cam1Settings, cam2Settings, scaleDetectObj):
		finalImage = Scanner.processImages(img, img2, cam1Settings, cam2Settings, scaleDetectObj)

		#Return stitched image, but doesn't have any contours on it currently
		return finalImage
