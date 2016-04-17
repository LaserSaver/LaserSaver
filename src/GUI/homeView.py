from appUtils import *

class HomeView(Frame):
	def __init__(self, master, controller, isReady, logoImg):
		''' The HomeView if there is no config file will not allow the user to start export,
			but only to calibrate the various models
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(HomeController object): The controller which will be in charge of the view
		    	isReady(boolean): Lets the view know if the user is ready to start the export json process
		    	logoImg(Img): The img used as the logo
		'''
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Welcome", font="-weight bold")
		promptLabel.pack(side=TOP)

		def configImgPanel(img, imgPanel):
			imgheight, imgwidth, channels = img.shape
			resizdeImg = AppUtils.converImgToTkinterImg(img, imgwidth, imgheight)
			imgPanel.configure(width=imgwidth, height=imgheight, image = resizdeImg)
			imgPanel.image = resizdeImg

		self.imgPanel = Label(self)
		configImgPanel(logoImg, self.imgPanel)
		self.imgPanel.bind("<Configure>", lambda e: configImgPanel(logoImg, self.imgPanel) )
		self.imgPanel.place(relx=0.5, rely=0.45,anchor=CENTER)

		self.calibrateButton = Button(self, text="Calibrate", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)

		self.startButton = Button(self, text="Scan Board", command=controller.startClicked)
		if not isReady:
			self.startButton.configure( state=DISABLED)
		self.startButton.pack(side=BOTTOM)
	

