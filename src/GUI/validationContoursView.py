from appUtils import *
from baseView import BaseView

class ValidationContoursView(BaseView):
	def __init__(self, master, controller, img):
		''' Sets up the validation contours view screen
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ValidationContoursController object): The controller which will be in charge of the view
		    	img(Image): The resulting image from the contours model processing
		'''
		BaseView.__init__(self, master)

		self.addTitle("Does this look okay?")


		def configImgPanel(img, imgPanel):
			resizdeImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-150)
			imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-150, relief=RIDGE, borderwidth=2, image = resizdeImg)
			imgPanel.image = resizdeImg

		self.imgPanel = Label(self)
		configImgPanel(img, self.imgPanel)
		self.imgPanel.bind("<Configure>", lambda e: configImgPanel(img, self.imgPanel) )
		self.imgPanel.pack(side=TOP)

		self.noButton = Button(self, text="No" , command=controller.noClicked)
		self.noButton.pack(side=BOTTOM)

		self.yesButton = Button(self, text="Yes", command=controller.yesClicked)
		self.yesButton.pack(side=BOTTOM)




		
