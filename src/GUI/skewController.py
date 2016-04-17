from appUtils import *
from skewView import SkewView
from skewModel import SkewModel 

class SkewController:
	def __init__(self, master):
		''' The skew controller in charge of updating the skew model
		 
			Args:
				master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		self.master = master

		self.photos = []
		self.model = SkewModel()

		self.view = SkewView(master, self)

		self.cam = AppUtils.getCam()
	
		self.view.pack(expand=YES,fill=BOTH)

		self.view.updateButtons(len(self.photos))

		self.continiousUpdatePanel()

	def continiousUpdatePanel(self):
		'''Calls on updatePanel continiously
		'''
		if not self.view.winfo_exists():
			#If view is removed stop updating the panel
			self.master.after_cancel(self.updatePanelID)
			return
		
		self.updatePanel()
		self.updatePanelID = self.master.after(AppUtils.framePerMillis,self.continiousUpdatePanel )

	def updatePanel(self):
		''' Updates the image in the video capture 
		'''
		imgtk = AppUtils.getTkinterImg(self.cam,self.view.videoCapturePanel.winfo_width(),self.view.videoCapturePanel.winfo_height())
		self.view.videoCapturePanel.configure(image = imgtk)
		self.view.videoCapturePanel.image = imgtk

	def undoClicked(self):
		'''When the undobutton is clicked removes one of the images from the list
		'''
		self.photos.pop()
		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

	def takingPictureEffect(self, case=0):
		'''This is used to create the flash effect when taking picture

			Args:
				case(int): The current step in the animation 
		'''
		if not self.view.winfo_exists():
			return 
		if case == 0:
			#Stopping video capture disable take photo button
			self.master.after_cancel(self.updatePanelID)
			self.view.photoButton.configure( state=DISABLED)
			self.master.after(50, self.takingPictureEffect, 1)
		elif case == 1:
			#Setting image to none
			self.view.videoCapturePanel.configure(image = None)
			self.view.videoCapturePanel.image = None
			self.master.after(50, self.takingPictureEffect, 2)
		else :
			self.view.photoButton.configure( state=NORMAL)
			self.continiousUpdatePanel()

	def startSkewCalibration(self):
		'''When the calibration button is clicked
		'''
		self.view.photoButton.pack_forget()
		self.view.undoButton.pack_forget()
		self.view.calibrateButton.pack_forget()
		
		progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
		progressbar.bind("<Configure>", lambda e: progressbar.configure(length=self.master.winfo_width()-50) )
		progressbar.pack(side=BOTTOM)
		progressbar.start()

		processingLabel = Label(self.view, text="Processing...")
		processingLabel.pack(side=BOTTOM)

		AppUtils.computeOnSeprateThread(self.master, self.calibrationDone, self.model.calculate ,[self.photos])

	def takePhotoClicked(self):
		'''When the take photo button is clicked
		'''
		self.takingPictureEffect()
		self.photos.append(AppUtils.getImg(self.cam))
		self.view.updateButtons(len(self.photos))
	


	def calibrationDone(self, img):
		'''Called back from the model processing
			
			Args:
				img(Image): The image returned from the model's processing
		'''
		self.view.destroy()
		#Had to import here to prevent cyclical refrencing
		from validationSkewController import ValidationSkewController
		ValidationSkewController(self.master, img)