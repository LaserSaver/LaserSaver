from appUtils import *
from contoursView import ContoursView
from contoursModel import ContoursModel

class ContoursController:
	def __init__(self, master):
		''' Sets up the contours view and initializes both cameras to use for video capture
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		self.master = master
		
		self.cam = AppUtils.getCam()

		self.model = ContoursModel()
	

		self.view = ContoursView(master, self)
		self.view.pack(expand=YES,fill=BOTH)
		self.continiousUpdatePanel()


	def takingPicturesEffect(self, case=0):
		'''This is used to create the flash effect when taking picture

			Args:
				case(int): The current step in the animation 
		'''
		if not self.view.winfo_exists():
			return 
		if case == 0:
			#Stopping video capture disable take photo button
			self.master.after_cancel(self.updatePanelID)
			self.master.after(50, self.takingPicturesEffect, 1)
		elif case == 1:
			#Setting image to none
			self.view.videoPanel.configure(image = None)
			self.view.videoPanel.image = None
			
			self.master.after(50, self.takingPicturesEffect, 2)
		else :
			self.continiousUpdatePanel()


	def continiousUpdatePanel(self):
		'''Calls on updatePanels continiously 
		'''
		if not self.view.winfo_exists():
			#If view is removed stop updating the panel
			self.master.after_cancel(self.updatePanelID)
			return
		self.updatePanel()
		#Update capture every 
		self.updatePanelID = self.master.after(AppUtils.framePerMillis, self.continiousUpdatePanel)

	def updatePanel(self):
		''' Updates the images in the video capture 
		'''
		imgtk = AppUtils.getTkinterImg(self.cam,self.view.videoPanel.winfo_width(),self.view.videoPanel.winfo_height())
		self.view.videoPanel.configure(image = imgtk)
		self.view.videoPanel.image = imgtk




	def takePhotosClicked(self):
		'''Takes two pictures and performs contours processing on them on seperate thread
		'''
		img = AppUtils.getImg(self.cam)
		self.takingPicturesEffect()

		#Submitting for calibration
		self.view.photosButton.pack_forget()
			
		progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
		progressbar.bind("<Configure>", lambda e: progressbar.configure(length=self.master.winfo_width()-50) )
		progressbar.pack(side=BOTTOM)
		progressbar.start()

		processingLabel = Label(self.view, text="Processing...")
		processingLabel.pack(side=BOTTOM)

		AppUtils.computeOnSeprateThread(self.master, self.processingDone, self.model.calculate ,[img])

	def processingDone(self, img):
		'''Moves to validation contoursView

			Args:
				img(Image): The image computed from the model function
		'''
		self.view.destroy()

		from validationContoursController import ValidationContoursController 
		ValidationContoursController(self.master,img)


		
