from appUtils import *
from validationScaleView import ValidationScaleView
from scaleController import ScaleController
from scaleModel import ScaleModel

class ValidationScaleController:
	def __init__(self, master, formParams, img):
		''' The validation scale controller in charge of asking the user whether the images he took are fit to
			be processed by the scale model
		 
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	formParams(Dictonary): The params that fill the form
		    	img(Image): Confirm taken image from camera
		'''
		self.master = master

		self.view = ValidationScaleView(master, self, img)
		self.view.pack(expand=YES,fill=BOTH)

		self.model = ScaleModel()

		self.formParams = formParams
		
		self.img = img

	def yesClicked(self):
		'''Yes button clicked start processing by the scale model'''
		self.view.yesButton.pack_forget()
		self.view.noButton.pack_forget()
			
		self.view.progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
		self.view.progressbar.bind("<Configure>", lambda e: self.view.progressbar.configure(length=self.master.winfo_width()-50) )
		self.view.progressbar.pack(side=BOTTOM)
		self.view.progressbar.start()

		AppUtils.computeOnSeprateThread(self.master, self.finishCalibrating, self.model.calculate ,[self.img, self.formParams['width'], self.formParams['height'], self.formParams['units']])

		self.view.processingLabel = Label(self.view, text="Processing...")
		self.view.processingLabel.pack(side=BOTTOM)

	def noClicked(self):
		'''No Button clicked go back to the previous step'''
		self.view.destroy()
		ScaleController(self.master, self.formParams)

	def finishCalibrating(self, wentWell):
		'''Called on when the scale model finished processing and updates the view accordingly

			Args:
				wentlWell(Bool): Tells the controller whether or not the scale model was sucessfully calibrated
		''' 
		self.view.processingLabel.pack_forget()
		self.view.progressbar.pack_forget()
		
		if wentWell:
			exitButton = Button(self.view, text="Return home", command=self.view.homeClicked)
			exitButton.pack(side=BOTTOM)

			self.view.processingLabel = Label(self.view, text="Congratulations, scale was sucessfully calibrated")
			self.view.processingLabel.pack(side=BOTTOM)

		else :
			redoButton = Button(self.view, text="Try again", command=self.noClicked)
			redoButton.pack(side=BOTTOM)

			self.view.processingLabel = Label(self.view, text="Uh oh, something went wrong")
			self.view.processingLabel.pack(side=BOTTOM)


		
