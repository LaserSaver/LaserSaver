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

		label = Label(self, text="Take phots" , font="-weight bold")
		label.pack(side=TOP)

		#Video Capture frame for both cameras
		self.frame = Label(self )
		self.frame.pack(side=TOP)


		panelWidth = (master.winfo_width()-10)/2
		panelHeight = (master.winfo_height() -100)

		self.videoPanel1 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel1.pack(side=LEFT)

		self.videoPanel2 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel2.pack(side=RIGHT)

		def resizeVideoCapturePanels(videoPanel1, videoPanel2,controller):
			controller.updatePanels()
			panelWidth = (master.winfo_width()-10)/2
			panelHeight = (master.winfo_height() -100)

			videoPanel1.configure(width=panelWidth, height=panelHeight)
			videoPanel2.configure(width=panelWidth, height=panelHeight)
			controller.updatePanels()

		self.frame.bind("<Configure>", lambda e: resizeVideoCapturePanels(self.videoPanel1, self.videoPanel2, controller) )

		self.photosButton = Button(self, text="Take photos", command=controller.takePhotosClicked)
		self.photosButton.pack(side=BOTTOM)
