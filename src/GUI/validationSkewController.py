from appUtils import *
from validationSkewView import ValidationSkewView
from skewController import SkewController
from scaleController import ScaleController

class ValidationSkewController:
	def __init__(self, master, img, camNumber):
		self.master = master

		self.camNumber = camNumber

		self.view = ValidationSkewView(master, self, img, camNumber)
		self.view.pack(expand=YES,fill=BOTH)

	def continueClicked(self):
		self.view.pack_forget()
		if self.camNumber < 1:
			SkewController(self.master, self.camNumber +1)
		else :
			ScaleController(self.master)


	def redoClicked(self):
		self.view.pack_forget()
		SkewController(self.master, self.camNumber)