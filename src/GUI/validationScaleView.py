from appUtils import *
from baseView import BaseView

class ValidationScaleView(BaseView):
	def __init__(self, master, controller, img, img2):
		''' Sets up the validation scale view screen
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ValidationScaleController object): The controller which will be in charge of the view
		    	img1(Image): Confirm taken image from camera 1
		    	img2(Image): Confirm taken image from camera 2 
		'''
		BaseView.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		self.frame = Label(self )
		self.frame.pack(side=TOP)


		panelWidth = (master.winfo_width()-10)/2
		panelHeight = (master.winfo_height() -115)

		self.imgPanel1 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.imgPanel1.pack(side=LEFT)

		self.imgPanel2 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.imgPanel2.pack(side=RIGHT)

		def resizeImgPanels(imgPanel1, imgPanel2,img1, img2):
			panelWidth = (master.winfo_width()-10)/2
			panelHeight = (master.winfo_height() -115)

			resizdeImg1 = AppUtils.converImgToTkinterImg(img1, panelWidth, panelHeight)
			imgPanel1.configure(width=panelWidth, height=panelHeight, image = resizdeImg1)
			imgPanel1.image = resizdeImg1

			resizdeImg2 = AppUtils.converImgToTkinterImg(img2, panelWidth, panelHeight)
			imgPanel2.configure(width=panelWidth, height=panelHeight, image = resizdeImg2)
			imgPanel2.image = resizdeImg2


		self.frame.bind("<Configure>", lambda e: resizeImgPanels(self.imgPanel1, self.imgPanel2, img, img2) )


		self.noButton = Button(self, text="No, return to scale calibration screen", command=controller.noClicked)
		self.noButton.pack(side=BOTTOM)

		self.yesButton = Button(self, text="Yes, start calibrating scale", command=controller.yesClicked)
		self.yesButton.pack(side=BOTTOM)