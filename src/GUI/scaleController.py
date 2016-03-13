from appUtils import *
from scaleView import ScaleView

class ScaleController:
	def __init__(self, master, formParams={'width':0.0,'height':0.0,'units':'centimeters'}):
		self.master = master

		self.cam1 = cv2.VideoCapture(0)

		#Change this to one for now same cam
		self.cam2 = cv2.VideoCapture(0)
	
		self.view = ScaleView(master, self, formParams)

		self.continiousUpdatePanel()
		self.view.pack()


	def continiousUpdatePanel(self):
		self.updatePanels()
		#Update capture every 50 milliseconds
		self.master.after(50, self.continiousUpdatePanel)

	def updatePanels(self):
		''' Updates the images in the video capture 
		'''
		imgtk = AppUtils.getTkinterImg(self.cam1,self.view.videoPanel1.winfo_width(),self.view.videoPanel1.winfo_height())
		self.view.videoPanel1.configure(image = imgtk)
		self.view.videoPanel1.image = imgtk

		imgtk = AppUtils.getTkinterImg(self.cam2,self.view.videoPanel2.winfo_width(),self.view.videoPanel2.winfo_height())
		self.view.videoPanel2.configure(image = imgtk)
		self.view.videoPanel2.image = imgtk



	def photosClicked(self):
		'''Move to validation export view
		'''
		self.view.pack_forget()
		img1 = AppUtils.getImg(self.cam1)
		img2 = AppUtils.getImg(self.cam2)

		formParams ={'width':float(self.view.widthInput.get()),'height':float(self.view.heightInput.get()),'units':self.view.unitsBox.get()}
		from validationScaleController import ValidationScaleController
		ValidationScaleController(self.master, formParams, img1, img2)

	