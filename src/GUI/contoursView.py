from appUtils import *
from baseView import BaseView

class ContoursView(BaseView):
	def __init__(self, master, controller):
		''' Sets up the contours view 
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ContoursController object): The controller which will be in charge of the view
		'''
		BaseView.__init__(self, master)

		self.addTitle("Scan Board")


		#Video Capture frame for both cameras
		self.videoPanel = Label(self )
		self.videoPanel.pack(side=TOP)

		def resizeVideoCapturePanels(videoPanel,controller):
			controller.updatePanel()
			panelWidth = (master.winfo_width()-10)
			panelHeight = (master.winfo_height() -140)

			videoPanel.configure(width=panelWidth, height=panelHeight)
			controller.updatePanel()

		self.videoPanel.bind("<Configure>", lambda e: resizeVideoCapturePanels(self.videoPanel, controller) )

		self.photosButton = Button(self, text="Take photo", command=controller.takePhotosClicked)
		self.photosButton.pack(side=BOTTOM)
