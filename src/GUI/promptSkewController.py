from appUtils import *
from promptSkewView import PromptSkewView 
from skewController import SkewController
from scaleController import ScaleController


class PromptSkewController:
	def __init__(self, master):
		self.master = master

		self.view = PromptSkewView(master, self)
		self.view.pack(expand=YES,fill=BOTH)


	def calibrateClicked(self):
		self.view.pack_forget()
		SkewController(self.master)

	def skipClicked(self):
		self.view.pack_forget()
		ScaleController(self.master)