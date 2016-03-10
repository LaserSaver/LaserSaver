from appUtils import *

class SkewView(Frame):
	def __init__(self, master, controller, cam_number):
		Frame.__init__(self, master)

		skewLabel = Label(self, text="Skew Calibration for Camera #" + str(cam_number+1), font="-weight bold")
		skewLabel.pack(side=TOP)


		def resizeVideoCapturePanel(videoCapturePanel, controller):
			videoCapturePanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-100)
			controller.updatePanel()

		self.videoCapturePanel = Label( self, width=master.winfo_width()-50, height=master.winfo_height()-100)
		self.videoCapturePanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoCapturePanel, controller) )
		self.videoCapturePanel.pack(side=TOP)

		self.undoButton = Button(self, text="Undo Last Photo",  state=DISABLED, command=controller.undoClicked)
		self.undoButton.pack(side=BOTTOM)

		self.photoButton = Button(self, text="Take Photo (0/" + str(controller.numberOfPhotosRequired) + ")", command=controller.takePhotoClicked)
		self.photoButton.pack(side=BOTTOM)



	def updateButtons(self, currentNumOfPhotos, totalPhotos):
		if currentNumOfPhotos < totalPhotos:
		    self.photoButton.config( text = "Take Photo ("+ str(currentNumOfPhotos) + "/" + str(totalPhotos) + ")")
		else:
		   	self.photoButton.config( text ="Finish Calibration")

		if currentNumOfPhotos == 0:
			self.undoButton.config( state=DISABLED)
		else:
			self.undoButton.config( state=NORMAL)




class SkewViewController:
	def __init__(self, master, cam_number):
		self.master = master

		self.numberOfPhotosRequired = 3
		self.photos = []

		self.view = SkewView(master, self, cam_number)
		self.cam = cv2.VideoCapture(cam_number)
		self.view.pack(expand=YES,fill=BOTH)

		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

		self.continiousUpdatePanel()

	def continiousUpdatePanel(self):
		self.updatePanel()
		self.master.after(50,self.continiousUpdatePanel )

	def updatePanel(self):
		imgtk = ImageTk.PhotoImage(AppUtils.getImg(self.view.videoCapturePanel.winfo_width(),self.view.videoCapturePanel.winfo_height(),self.cam))
		self.view.videoCapturePanel.configure(image = imgtk)
		self.view.videoCapturePanel.image = imgtk

	def undoClicked(self):
		self.photos.pop()
		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

	def takePhotoClicked(self):
		if len(self.photos) < self.numberOfPhotosRequired:
			#Taking a photo
			self.photos.append(1)
		else:
			#Submitting for calibration
			self.master
		
		self.view.updateButtons(len(self.photos), self.numberOfPhotosRequired)

