from appUtils import *
from scaleView import ScaleView

class ScaleController:
	def __init__(self, master, formParams={'width':0.0,'height':0.0,'units':'cm'}):
		''' The scale controller in charge of updating the scale model
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	formParams(Dictonary): The params that fill the form
		'''
		self.master = master

		self.cam = AppUtils.getCam()
	
		self.view = ScaleView(master, self, formParams)
		self.view.pack(expand=YES,fill=BOTH)

		self.continiousUpdatePanel()


	def continiousUpdatePanel(self):
		'''Calls on updatePanels continiously 
		'''
		if self.view.winfo_manager() == "":
			#If view is removed stop updating the panel
			self.master.after_cancel(self.updatePanelID)
			return

		self.updatePanel()
		self.updatePanelID = self.master.after(AppUtils.framePerMillis, self.continiousUpdatePanel)

	def updatePanel(self):
		''' Updates the images in the video capture 
		'''
		imgtk = AppUtils.getTkinterImg(self.cam,self.view.videoPanel.winfo_width(),self.view.videoPanel.winfo_height())
		self.view.videoPanel.configure(image = imgtk)
		self.view.videoPanel.image = imgtk



	def photosClicked(self):
		'''Move to validation export view
		'''
		self.view.pack_forget()
		img = AppUtils.getImg(self.cam)

		formParams ={'width':float(self.view.widthInput.get()),'height':float(self.view.heightInput.get()),'units':self.view.unitsBox.get()}
		from validationScaleController import ValidationScaleController
		ValidationScaleController(self.master, formParams, img)

	