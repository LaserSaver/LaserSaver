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

		self.addTitle("Skew Calibration")

		def resizeVideoCapturePanel(videoCapturePanel, controller):
			controller.updatePanel()
			videoCapturePanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-175)
			controller.updatePanel()

		self.videoCapturePanel = Label( self, width=master.winfo_width()-50, height=master.winfo_height()-175 , relief=RIDGE, borderwidth=2)
		self.videoCapturePanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoCapturePanel, controller) )
		self.videoCapturePanel.pack(side=TOP)

		self.undoButton = Button(self, text="Undo last photo",  state=DISABLED, command=controller.undoClicked)
		self.undoButton.pack(side=BOTTOM)

		self.photoButton = Button(self, text="Take photo", command=controller.takePhotoClicked)
		self.photoButton.pack(side=BOTTOM)

		self.calibrateButton = Button(self, text="Start Skew Calibration", command=controller.startSkewCalibration)
		self.calibrateButton.pack(side=BOTTOM)



	def updateButtons(self, currentNumOfPhotos):
		'''An update buttons function that updates the buttons everytime there is an update with the number of photos takes

			Args:
				currentNumOfPhotos(int): The total number of photos currently taken
				totalPhotos(int): The total amount of photos needed to complete calibration
		'''
		self.photoButton.configure( text = "Take photo (Taken "+ str(currentNumOfPhotos) + " Photos)")
		
		if currentNumOfPhotos == 0:
			self.undoButton.configure( state=DISABLED)
		else:
			self.undoButton.configure( state=NORMAL)


		
