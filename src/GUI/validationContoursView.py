from appUtils import *
from contoursView import ContoursViewController
from exportView import ExportViewController

class ValidationContoursView(Frame):
	def __init__(self, master, controller, img, camNumber):
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		def configImgPanel(img, imgPanel):
			resizdeImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-100)
			imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-100, relief=RIDGE, borderwidth=2, image = resizdeImg)
			imgPanel.image = resizdeImg

		self.imgPanel = Label(self)
		configImgPanel(img, self.imgPanel)
		self.imgPanel.bind("<Configure>", lambda e: configImgPanel(img, self.imgPanel) )
		self.imgPanel.pack(side=TOP)

		self.redoButton = Button(self, text="No, return to calibrating camera #" + str(camNumber +1), command=controller.redoClicked)
		self.redoButton.pack(side=BOTTOM)

		if camNumber < 1:
			continueText = "Yes, continue to calibrating camera #" + str(camNumber +2)
		else :
			continueText = "Yes, continue to export screen"


		self.continuteButton = Button(self, text=continueText, command=controller.continueClicked)
		self.continuteButton.pack(side=BOTTOM)




class ValidationContoursViewController:
	def __init__(self, master, img, camNumber):
		self.master = master

		self.camNumber = camNumber

		self.view = ValidationContoursView(master, self, img, camNumber)
		self.view.pack(expand=YES,fill=BOTH)

	def continueClicked(self):
		self.view.pack_forget()
		if self.camNumber < 1:
			ContoursViewController(self.master, self.camNumber +1)
		else :
			ExportViewController(self.master)


	def redoClicked(self):
		self.view.pack_forget()
		ContoursViewController(self.master, self.camNumber)

		
