from appUtils import *
from validationSkewView import ValidationSkewView
from skewController import SkewController
from scaleController import ScaleController

class ValidationSkewController:
	def __init__(self, master, img, camNumber):
		''' The validation skew controller in charge of validating with the user whether processing 
			was done correct by the Skew Model
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	img(Image): The resulting image from the skew model processing
		    	camNumber(Int): Current camera that is being calibrated
		'''
		self.master = master

		self.camNumber = camNumber

		self.view = ValidationSkewView(master, self, img, camNumber)
		self.view.pack(expand=YES,fill=BOTH)

	def continueClicked(self):
		'''Continue button clicked either goes on to calibrate the next camera or goes on to scale calibration'''
		self.view.pack_forget()
		if self.camNumber < 1:
			SkewController(self.master, self.camNumber +1)
		else :
			ScaleController(self.master)


	def redoClicked(self):
		'''The redo button clicked goes back to the previous step'''
		self.view.pack_forget()
		SkewController(self.master, self.camNumber)