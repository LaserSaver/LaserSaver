from appUtils import *
from baseView import BaseView

class PromptSkewView(BaseView):
	def __init__(self, master, controller):
		''' Sets up The PromptSkewView 
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(PromptSkewController object): The controller which will be in charge of the view
		'''
		BaseView.__init__(self, master)

		promptLabel = Label(self, text="Would you like to calibrate for skew?", font="-weight bold")
		promptLabel.pack(side=TOP)

		instructions = Message(self, text="Calibration of skew bleh bleh aksjdhfjdksahfjdsnfjkadbncjkdsabcjkdsbckdsacdlsakcjdslakbcvdsklavjbdskjalvcbdsjakvbsdkjavbsdkavjbdsakjv", relief=RIDGE, borderwidth=2)
		instructions.pack(side=TOP)

		#Configure is for when window is resized 
		instructions.bind("<Configure>", lambda e: instructions.configure(width=master.winfo_width()-50))


		self.skipButton = Button(self, text="Skip", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)
		
		self.calibrateButton = Button(self, text="Calibrate skew", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)
