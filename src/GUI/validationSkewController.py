from appUtils import *
from validationSkewView import ValidationSkewView
from skewController import SkewController
from scaleController import ScaleController

class ValidationSkewController:
	def __init__(self, master, img):
		''' The validation skew controller in charge of validating with the user whether processing 
			was done correct by the Skew Model
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	img(Image): The resulting image from the skew model processing
		'''
		self.master = master


		self.view = ValidationSkewView(master, self, img)
		self.view.pack(expand=YES,fill=BOTH)

	def continueClicked(self):
		'''Continue button clicked goes on to scale calibration'''
		self.view.destroy()
		ScaleController(self.master)


	def redoClicked(self):
		'''The redo button clicked goes back to the previous step'''
		self.view.destroy()
		SkewController(self.master)