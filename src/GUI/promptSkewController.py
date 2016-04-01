from appUtils import *
from promptSkewView import PromptSkewView 
from skewController import SkewController
from scaleController import ScaleController


class PromptSkewController:
	def __init__(self, master):
		''' This controller is in charge of prompting the user to start skew calibration 
		
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		self.master = master

		self.view = PromptSkewView(master, self)
		self.view.pack(expand=YES,fill=BOTH)


	def calibrateClicked(self):
		'''Called on when calibration is clicked goes to the next step
		'''
		self.view.pack_forget()
		SkewController(self.master)

	def skipClicked(self):
		'''Called on when skip is clicked skips to scale detection
		'''
		self.view.pack_forget()
		ScaleController(self.master)