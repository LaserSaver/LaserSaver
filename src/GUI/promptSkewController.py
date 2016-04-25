from appUtils import *
from promptSkewView import PromptSkewView 
from skewController import SkewController
from scaleController import ScaleController
import tkMessageBox

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
		self.view.destroy()
		SkewController(self.master)

	def skipClicked(self):
		'''Called on when skip is clicked skips to scale detection
		'''
		self.view.destroy()
		ScaleController(self.master)
	
	def deleteClicked(self):
		'''Called on when delete button is clicked
		'''
	 	if tkMessageBox.askyesno("Warning", "Are you sure you want to delete previous skew calibration?"):
			print("YO")