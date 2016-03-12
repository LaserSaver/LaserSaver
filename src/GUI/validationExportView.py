from appUtils import *
from exportView import ExportViewController
from exportModel import ExportModel

class ValidationExportView(Frame):
	def __init__(self, master, controller, img, img2):
		Frame.__init__(self, master)

		promptLabel = Label(self, text="Does this look okay?", font="-weight bold")
		promptLabel.pack(side=TOP)


		self.frame = Label(self )
		self.frame.pack(side=TOP)


		panelWidth = (master.winfo_width()-50)
		panelHeight = (master.winfo_height() -100)/2

		self.imgPanel1 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.imgPanel1.pack(side=TOP)

		self.imgPanel2 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.imgPanel2.pack(side=TOP)

		def resizeImgPanels(imgPanel1, imgPanel2,img1, img2):
			panelWidth = (master.winfo_width()-50)
			panelHeight = (master.winfo_height() -100)/2

			resizdeImg1 = AppUtils.converImgToTkinterImg(img1, panelWidth, panelHeight)
			imgPanel1.configure(width=panelWidth, height=panelHeight, image = resizdeImg1)
			imgPanel1.image = resizdeImg1

			resizdeImg2 = AppUtils.converImgToTkinterImg(img2, panelWidth, panelHeight)
			imgPanel2.configure(width=panelWidth, height=panelHeight, image = resizdeImg2)
			imgPanel2.image = resizdeImg2


		self.frame.bind("<Configure>", lambda e: resizeImgPanels(self.imgPanel1, self.imgPanel2, img, img2) )


		self.redoButton = Button(self, text="No, return to export screen", command=controller.redoClicked)
		self.redoButton.pack(side=BOTTOM)

		self.expotButton = Button(self, text="Yes, start export", command=controller.exportClicked)
		self.expotButton.pack(side=BOTTOM)


class ValidationExportViewController:
	def __init__(self, master, formParams, img1, img2):
		self.master = master

		self.view = ValidationExportView(master, self, img1, img2)
		self.view.pack(expand=YES,fill=BOTH)

		self.formParams = formParams
		self.img1 = img1
		self.img2 = img2

	def exportClicked(self):
		#Submitting for calibration
		self.view.expotButton.pack_forget()
		self.view.redoButton.pack_forget()
			
		self.view.progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=self.master.winfo_width()-50, mode='determinate')
		self.view.progressbar.bind("<Configure>", lambda e: self.view.progressbar.configure(length=self.master.winfo_width()-50) )
		self.view.progressbar.pack(side=BOTTOM)
		self.view.progressbar.start()

		AppUtils.computeOnSeprateThread(self.master, self.finishExport, ExportModel().calculate ,[self.img1, self.img2, self.formParams['width'], self.formParams['height'], self.formParams['units']])

		self.view.processingLabel = Label(self.view, text="Processing...")
		self.view.processingLabel.pack(side=BOTTOM)

	def redoClicked(self):
		self.view.pack_forget()
		ExportViewController(self.master, self.formParams)

	def finishExport(self, wentWell):
		self.view.processingLabel.pack_forget()
		self.view.progressbar.pack_forget()
		if wentWell:
			exitButton = Button(self.view, text="Exit", command=self.master.destroy)
			exitButton.pack(side=BOTTOM)

			self.view.processingLabel = Label(self.view, text="Congratulations, data was exported successfully")
			self.view.processingLabel.pack(side=BOTTOM)

		else :
			redoButton = Button(self.view, text="Try again", command=self.redoClicked)
			redoButton.pack(side=BOTTOM)

			self.view.processingLabel = Label(self.view, text="Uh oh, something went wrong")
			self.view.processingLabel.pack(side=BOTTOM)


		
