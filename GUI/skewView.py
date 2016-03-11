from appUtils import *
from skewModel import SkewModel 

class SkewView(Frame):
	def __init__(self, master, controller, camNumber):
		Frame.__init__(self, master)

		skewLabel = Label(self, text="Skew Calibration for Camera #" + str(camNumber+1), font="-weight bold")
		skewLabel.pack(side=TOP)


		def resizeVideoCapturePanel(videoCapturePanel, controller):
			videoCapturePanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-100)
			controller.updatePanel()

		self.videoCapturePanel = Label( self, width=master.winfo_width()-50, height=master.winfo_height()-100 , relief=RIDGE, borderwidth=2)
		self.videoCapturePanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoCapturePanel, controller) )
		self.videoCapturePanel.pack(side=TOP)

		self.undoButton = Button(self, text="Undo Last Photo",  state=DISABLED, command=controller.undoClicked)
		self.undoButton.pack(side=BOTTOM)

		self.photoButton = Button(self, text="Take Photo (0/" + str(controller.numberOfPhotosRequired) + ")", command=controller.takePhotoClicked)
		self.photoButton.pack(side=BOTTOM)



	def updateButtons(self, currentNumOfPhotos, totalPhotos):
		if currentNumOfPhotos < totalPhotos:
		    self.photoButton.configure( text = "Take Photo ("+ str(currentNumOfPhotos) + "/" + str(totalPhotos) + ")")
		else:
		   	self.photoButton.configure( text ="Finish Calibration")

		if currentNumOfPhotos == 0:
			self.undoButton.configure( state=DISABLED)
		else:
			self.undoButton.configure( state=NORMAL)




class SkewViewController:
	def __init__(self, master, camNumber):
		self.master = master
		self.camNumber = camNumber;

		self.numberOfPhotosRequired = 3
		self.photos = []

		self.view = SkewView(master, self, camNumber)
		self.cam = cv2.VideoCapture(camNumber)
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

			AppUtils.computeOnSeprateThread(self.master, self.calibrationDone, SkewModel().calculate ,[self.photos])

			processingLabel = Label(self.view, text="Processing...")
			processingLabel.pack(side=BOTTOM)

	def calibrationDone(self, img):
		#Had to import here to prevent cyclical refrencing
		from validationSkewView import ValidationSkewViewController
		self.view.pack_forget()
		ValidationSkewViewController(self.master, img, self.camNumber)
		
