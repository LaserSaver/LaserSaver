from appUtils import *
from homeView import HomeView
from homeModel import HomeModel

class HomeController:
	def __init__(self, master):
		''' The HomeController if there is no config file will not allow the user to start export,
			but only to calibrate the various models
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		self.master = master
		self.model = HomeModel()


		#Assume there is a config file for now
		isReady = self.model.doesScaleExist()
		self.view = HomeView(master, self, isReady)
		self.view.pack(expand=YES,fill=BOTH)

	def startClicked(self):
		'''Called on when the start button is clicked start the json export process
		'''
		self.view.pack_forget()

		#To avoid cyclical imports
		from contoursController import ContoursController
		ContoursController(self.master)

	def calibrateClicked(self):
		'''Called when the calibrate button is clicked starts the calibration process
		'''
		self.view.pack_forget()

		#To avoid cyclical imports
		from promptSkewController import PromptSkewController
		PromptSkewController(self.master)
