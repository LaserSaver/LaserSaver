from appUtils import *
from baseView import BaseView

class ValidationScaleView(BaseView):
	def __init__(self, master, controller, img):
		''' Sets up the validation scale view screen
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ValidationScaleController object): The controller which will be in charge of the view
		    	img(Image): Confirm taken image from camera 
		'''
		BaseView.__init__(self, master)

		self.addTitle("Does this look okay?")


		self.imgPanel = Label(self )
		self.imgPanel.pack(side=TOP)

		def resizeImgPanel(imgPanel,img):
			panelWidth = (master.winfo_width()-10)
			panelHeight = (master.winfo_height() -145)

			resizdeImg = AppUtils.converImgToTkinterImg(img, panelWidth, panelHeight)
			imgPanel.configure(width=panelWidth, height=panelHeight, image = resizdeImg)
			imgPanel.image = resizdeImg


		self.imgPanel.bind("<Configure>", lambda e: resizeImgPanel(self.imgPanel, img) )


		self.noButton = Button(self, text="No, return to scale calibration screen", command=controller.noClicked)
		self.noButton.pack(side=BOTTOM)

		self.yesButton = Button(self, text="Yes, start calibrating scale", command=controller.yesClicked)
		self.yesButton.pack(side=BOTTOM)