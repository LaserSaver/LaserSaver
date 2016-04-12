from appUtils import *
from baseView import BaseView

class SkewView(BaseView):
	def __init__(self, master, controller):
		''' Sets up the skew view
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(SkewController object): The controller which will be in charge of the view
		'''
		BaseView.__init__(self, master)

		skewLabel = Label(self, text="Skew calibration", font="-weight bold")
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
		'''An update buttons function that updates the buttons everytime there is an update with the number of photos takes

			Args:
				currentNumOfPhotos(int): The total number of photos currently taken
				totalPhotos(int): The total amount of photos needed to complete calibration
		'''
		if currentNumOfPhotos < totalPhotos:
		    self.photoButton.configure( text = "Take photo ("+ str(currentNumOfPhotos) + "/" + str(totalPhotos) + ")")
		else:
		   	self.photoButton.configure( text ="Start calibration")

		if currentNumOfPhotos == 0:
			self.undoButton.configure( state=DISABLED)
		else:
			self.undoButton.configure( state=NORMAL)


		
