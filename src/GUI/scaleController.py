from appUtils import *
from scaleView import ScaleView

class ScaleController:
	def __init__(self, master, formParams={'width':0.0,'height':0.0,'units':'centimeters'}):
		self.master = master

		self.cam1 = AppUtils.getCam1()
		self.cam2 = AppUtils.getCam2()
	
		self.view = ScaleView(master, self, formParams)
		self.view.pack(expand=YES,fill=BOTH)

		self.continiousUpdatePanel()


	def continiousUpdatePanel(self):
		if self.view.winfo_manager() == "":
			#If view is removed stop updating the panel
			self.master.after_cancel(self.updatePanelID)
			return

		self.updatePanels()
		#Update capture every 50 milliseconds
		self.updatePanelID = self.master.after(50, self.continiousUpdatePanel)

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

	