from appUtils import *
from validationContoursView import ValidationContoursView
from contoursController import ContoursController
from exportController import ExportController

class ValidationContoursController:
	def __init__(self, master, img):
		''' The validation contours controller in charge of validating with the user whether processing 
			was done correct by the Contours Model
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	img(Image): The resulting image from the contours model processing
		'''
		self.master = master

		self.view = ValidationContoursView(master, self, img)
		self.view.pack(expand=YES,fill=BOTH)

	def yesClicked(self):
		'''When the yes button is clicked goes on to the next step'''
		self.view.pack_forget()
		ExportController(self.master)

	def noClicked(self):
		'''When the no button is clicked goes back to a previous step'''
		self.view.pack_forget()
		ContoursController(self.master)