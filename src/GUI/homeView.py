from appUtils import *

class HomeView(Frame):
	def __init__(self, master, controller, isReady):
		''' The HomeView if there is no config file will not allow the user to start export,
			but only to calibrate the various models
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(HomeController object): The controller which will be in charge of the view
		    	isReady(boolean): Lets the view know if the user is ready to start the export json process
		'''
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Welcome", font="-weight bold")
		promptLabel.pack(side=TOP)

		self.calibrateButton = Button(self, text="Calibrate", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)

		self.startButton = Button(self, text="Scan Board", command=controller.startClicked)
		if not isReady:
			self.startButton.configure( state=DISABLED)
		self.startButton.pack(side=BOTTOM)
	

