from appUtils import *
from validationContoursView import ValidationContoursView
from contoursController import ContoursController
from exportController import ExportController

class ValidationContoursController:
	def __init__(self, master, img):
		self.master = master

		self.view = ValidationContoursView(master, self, img)
		self.view.pack(expand=YES,fill=BOTH)

	def yesClicked(self):
		self.view.pack_forget()
		ExportController(self.master)

	def noClicked(self):
		self.view.pack_forget()
		ContoursController(self.master)