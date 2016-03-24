from appUtils import *

class HomeView(Frame):
	def __init__(self, master, controller, isReady):
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Welcome", font="-weight bold")
		promptLabel.pack(side=TOP)

		self.calibrateButton = Button(self, text="Calibrate", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)

		self.startButton = Button(self, text="Start", command=controller.startClicked)
		if not isReady:
			self.startButton.configure( state=DISABLED)
		self.startButton.pack(side=BOTTOM)
	

