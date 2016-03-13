from appUtils import *
from skewView import SkewView
from skewModel import SkewModel 

class SkewController:
	def __init__(self, master, camNumber=0):
		self.master = master
		self.camNumber = camNumber;

		self.numberOfPhotosRequired = 3
		self.photos = []
		self.model = SkewModel()

		self.view = SkewView(master, self, camNumber)

		#Change 0 to cam number currently only have one camera
		self.cam = cv2.VideoCapture(0)
		self.view.pack(expand=YES,fill=BOTH)

		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

		self.continiousUpdatePanel()

	def continiousUpdatePanel(self):
		self.updatePanel()
		self.updatePanelID = self.master.after(50,self.continiousUpdatePanel )

	def updatePanel(self):
		imgtk = AppUtils.getTkinterImg(self.cam,self.view.videoCapturePanel.winfo_width(),self.view.videoCapturePanel.winfo_height())
		self.view.videoCapturePanel.configure(image = imgtk)
		self.view.videoCapturePanel.image = imgtk

	def undoClicked(self):
		self.photos.pop()
		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

	def takingPictureEffect(self, case=0):
		'''
			This is used to create the flash effect when taking picture 
		'''
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


	def takePhotoClicked(self):
		if len(self.photos) < self.numberOfPhotosRequired:
			#Taking a photo
			self.takingPictureEffect()
			self.photos.append(AppUtils.getImg(self.cam))
			self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)
		else:
			#Submitting for calibration
			self.view.photoButton.pack_forget()
			self.view.undoButton.pack_forget()
			
			progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
			progressbar.bind("<Configure>", lambda e: progressbar.configure(length=self.master.winfo_width()-50) )
			progressbar.pack(side=BOTTOM)
			progressbar.start()

			AppUtils.computeOnSeprateThread(self.master, self.calibrationDone, self.model.calculate ,[self.photos])

			processingLabel = Label(self.view, text="Processing...")
			processingLabel.pack(side=BOTTOM)

	def calibrationDone(self, img):
		#Had to import here to prevent cyclical refrencing
		from validationSkewController import ValidationSkewController
		self.view.pack_forget()
		ValidationSkewController(self.master, img, self.camNumber)