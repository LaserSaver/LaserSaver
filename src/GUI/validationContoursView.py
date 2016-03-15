from appUtils import *
from baseView import BaseView

class ValidationContoursView(BaseView):
	def __init__(self, master, controller, img):
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

		self.noButton = Button(self, text="No" , command=controller.noClicked)
		self.noButton.pack(side=BOTTOM)

		self.yesButton = Button(self, text="Yes", command=controller.yesClicked)
		self.yesButton.pack(side=BOTTOM)




		
