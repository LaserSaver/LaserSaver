from appUtils import *
from skewView import SkewViewController
from contoursView import ContoursViewController

class ValidationSkewView(Frame):
	def __init__(self, master, controller, img, camNumber):
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		def configImgPanel(img, imgPanel):
			resizdeImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-125)
			imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-125, relief=RIDGE, borderwidth=2, image = resizdeImg)
			imgPanel.image = resizdeImg

		self.imgPanel = Label(self)
		configImgPanel(img, self.imgPanel)
		self.imgPanel.bind("<Configure>", lambda e: configImgPanel(img, self.imgPanel) )
		self.imgPanel.pack(side=TOP)


		self.skipButton = Button(self, text="Skip for now", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)

		self.redoButton = Button(self, text="No, return to calibrating camera #" + str(camNumber +1), command=controller.redoClicked)
		self.redoButton.pack(side=BOTTOM)

		if camNumber < 1:
			continueText = "Yes, continue to calibrating camera #" + str(camNumber +2)
		else :
			continueText = "Yes, continue to contours calibration"


		self.continuteButton = Button(self, text=continueText, command=controller.continueClicked)
		self.continuteButton.pack(side=BOTTOM)




class ValidationSkewViewController:
	def __init__(self, master, img, camNumber):
		self.master = master

		self.camNumber = camNumber

		self.view = ValidationSkewView(master, self, img, camNumber)
		self.view.pack(expand=YES,fill=BOTH)

	def continueClicked(self):
		self.view.pack_forget()
		if self.camNumber < 1:
			SkewViewController(self.master, self.camNumber +1)
		else :
			ContoursViewController(self.master)


	def redoClicked(self):
		self.view.pack_forget()
		SkewViewController(self.master, self.camNumber)

	def skipClicked(self):
		self.view.pack_forget()
		ContoursViewController(self.master)
		
