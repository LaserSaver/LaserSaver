from appUtils import *
from homeView import HomeView

class HomeController:
	def __init__(self, master):
		self.master = master

		#Assume there is a config file for now
		isReady = True
		self.view = HomeView(master, self, isReady)
		self.view.pack(expand=YES,fill=BOTH)

	def startClicked(self):
		self.view.pack_forget()

		#To avoid cyclical imports
		from contoursController import ContoursController
		ContoursController(self.master)

	def calibrateClicked(self):
		self.view.pack_forget()

		#To avoid cyclical imports
		from promptSkewController import PromptSkewController
		PromptSkewController(self.master)
