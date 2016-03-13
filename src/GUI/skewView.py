from appUtils import *
from baseView import BaseView

class SkewView(BaseView):
	def __init__(self, master, controller, camNumber):
		BaseView.__init__(self, master)

		skewLabel = Label(self, text="Skew calibration for camera #" + str(camNumber+1), font="-weight bold")
		skewLabel.pack(side=TOP)


		def resizeVideoCapturePanel(videoCapturePanel, controller):
			controller.updatePanel()
			videoCapturePanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-115)
			controller.updatePanel()

		self.videoCapturePanel = Label( self, width=master.winfo_width()-50, height=master.winfo_height()-115 , relief=RIDGE, borderwidth=2)
		self.videoCapturePanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoCapturePanel, controller) )
		self.videoCapturePanel.pack(side=TOP)

		self.undoButton = Button(self, text="Undo last photo",  state=DISABLED, command=controller.undoClicked)
		self.undoButton.pack(side=BOTTOM)

		self.photoButton = Button(self, text="Take photo (0/" + str(controller.numberOfPhotosRequired) + ")", command=controller.takePhotoClicked)
		self.photoButton.pack(side=BOTTOM)



	def updateButtons(self, currentNumOfPhotos, totalPhotos):
		if currentNumOfPhotos < totalPhotos:
		    self.photoButton.configure( text = "Take photo ("+ str(currentNumOfPhotos) + "/" + str(totalPhotos) + ")")
		else:
		   	self.photoButton.configure( text ="Start calibration")

		if currentNumOfPhotos == 0:
			self.undoButton.configure( state=DISABLED)
		else:
			self.undoButton.configure( state=NORMAL)


		
