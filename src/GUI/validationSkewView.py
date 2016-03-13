from appUtils import *
from baseView import BaseView

class ValidationSkewView(BaseView):
	def __init__(self, master, controller, img, camNumber):
		BaseView.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		def configImgPanel(img, imgPanel):
			resizdeImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-145)
			imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-145, relief=RIDGE, borderwidth=2, image = resizdeImg)
			imgPanel.image = resizdeImg

		self.imgPanel = Label(self)
		configImgPanel(img, self.imgPanel)
		self.imgPanel.bind("<Configure>", lambda e: configImgPanel(img, self.imgPanel) )
		self.imgPanel.pack(side=TOP)


		self.skipButton = Button(self, text="Skip", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)

		self.redoButton = Button(self, text="No, return to calibrating camera #" + str(camNumber +1), command=controller.redoClicked)
		self.redoButton.pack(side=BOTTOM)

		if camNumber < 1:
			continueText = "Yes, continue to calibrating camera #" + str(camNumber +2)
		else :
			continueText = "Yes, continue to scale calibration"


		self.continuteButton = Button(self, text=continueText, command=controller.continueClicked)
		self.continuteButton.pack(side=BOTTOM)


