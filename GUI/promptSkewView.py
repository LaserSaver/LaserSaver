from appUtils import *
from contoursView import ContoursViewController 
from skewView import SkewViewController

class PromptSkewView(Frame):
	def __init__(self, master, controller):
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Would you like to calibrate for skew?", font="-weight bold")
		promptLabel.pack(side=TOP)

		instructions = Message(self, text="Calibration of skew bleh bleh aksjdhfjdksahfjdsnfjkadbncjkdsabcjkdsbckdsacdlsakcjdslakbcvdsklavjbdskjalvcbdsjakvbsdkjavbsdkavjbdsakjv", relief=RIDGE, borderwidth=2)
		instructions.pack(side=TOP)

		#Configure is for when window is resized 
		instructions.bind("<Configure>", lambda e: instructions.configure(width=master.winfo_width()-50))


		self.skipButton = Button(self, text="Skip For Now", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)
		
		self.calibrateButton = Button(self, text="Calibrate Skew", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)



class PromptSkewViewController:
	def __init__(self, master):
		self.master = master

		self.view = PromptSkewView(master, self)
		self.view.pack(expand=YES,fill=BOTH)


	def calibrateClicked(self):
		self.view.pack_forget()
		SkewViewController(self.master, 0)

	def skipClicked(self):
		self.view.pack_forget()
		ContoursViewController(self.master)