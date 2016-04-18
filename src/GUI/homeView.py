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
		helv54 = tkFont.Font(family='Helvetica',size=54) 
		promptLabel = Label(self, text="LaserSaver", font="-weight bold", pady=20 )
		promptLabel['font'] = helv54
		promptLabel.pack(side=TOP)

		self.imgPanel = Label(self)
		self.imgPanel.configure( image = logoImg,background=self["bg"])
		self.imgPanel.image = logoImg
		self.imgPanel.place(relx=0.5, rely=0.45,anchor=CENTER)

		helv18 = tkFont.Font(family='Helvetica',size=18) 

		self.calibrateButton = Button(self, text="Calibrate", command=controller.calibrateClicked,pady=5)
		self.calibrateButton['font'] = helv18
		self.calibrateButton.pack(side=BOTTOM)

		self.startButton = Button(self, text="Scan Board", command=controller.startClicked, pady=5)

		self.startButton ['font'] = helv18

		if not isReady:
			self.startButton.configure( state=DISABLED)
		self.startButton.pack(side=BOTTOM)
	

