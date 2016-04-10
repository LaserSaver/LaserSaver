from appUtils import *
from baseView import BaseView

class ValidationSkewView(BaseView):
	def __init__(self, master, controller, img, camNumber):
		''' Sets up the skew validation contours view screen
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ValidationSkewController object): The controller which will be in charge of the view
		    	img(Image): The resulting image from the skew model processing
		    	camNumber(Int): Current camera that is being calibrated
		'''
		BaseView.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		def configImgPanel(img, imgPanel):
			resizdeImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-115)
			imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-115, relief=RIDGE, borderwidth=2, image = resizdeImg)
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
			continueText = "Yes, continue to scale calibration"


		self.continuteButton = Button(self, text=continueText, command=controller.continueClicked)
		self.continuteButton.pack(side=BOTTOM)


