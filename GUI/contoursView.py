from appUtils import *
from contoursModel import ContoursModel

class ContoursView(Frame):
	def __init__(self, master, controller, camNumber):
		Frame.__init__(self, master)

		skewLabel = Label(self, text="Calibrating Contours for Camera #" + str(camNumber+1) , font="-weight bold")
		skewLabel.pack(side=TOP)


		boardLabel = Label(self, text="Place Board in Bed" , font="-weight bold")
		boardLabel.pack(side=TOP)



		def resizeVideoCapturePanel(videoCapturePanel, controller):
			videoCapturePanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-100)
			controller.updatePanel()

		self.videoCapturePanel = Label( self, width=master.winfo_width()-50, height=master.winfo_height()-100 , relief=RIDGE, borderwidth=2)
		self.videoCapturePanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoCapturePanel, controller) )
		self.videoCapturePanel.pack(side=TOP)

		self.photoButton = Button(self, text="Take Photo", command=controller.takePhotoClicked)
		self.photoButton.pack(side=BOTTOM)


class ContoursViewController:
	def __init__(self, master, camNumber):
		self.master = master

		self.camNumber = camNumber
		#Change 0 to cam number currently only have one camera
		self.cam = cv2.VideoCapture(0)

		self.view = ContoursView(master, self, camNumber)
		self.view.pack()
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
			self.master.after(50, self.takingPictureEffect, 1)
		elif case == 1:
			#Setting image to none
			self.view.videoCapturePanel.configure(image = None)
			self.view.videoCapturePanel.image = None
			self.master.after(50, self.takingPictureEffect, 2)
		else :
			self.continiousUpdatePanel()


	def takePhotoClicked(self):
		#Submitting for calibration
		self.view.photoButton.pack_forget()

		self.takingPictureEffect()
				
		progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
		progressbar.bind("<Configure>", lambda e: progressbar.configure(length=self.master.winfo_width()-50) )
		progressbar.pack(side=BOTTOM)
		progressbar.start()

		img = AppUtils.getImg(self.cam)
		AppUtils.computeOnSeprateThread(self.master, self.calibrationDone, ContoursModel().calculate, [img])

		processingLabel = Label(self.view, text="Processing...")
		processingLabel.pack(side=BOTTOM)

	def calibrationDone(self, img):
		#Had to import here to prevent cyclical refrencing
		from validationContoursView import ValidationContoursViewController
		self.view.pack_forget()
		ValidationContoursViewController(self.master, img, self.camNumber)
		
