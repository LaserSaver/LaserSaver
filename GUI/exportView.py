from appUtils import *

class ExportView(Frame):
	def __init__(self, master, controller,formParams):
		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		Frame.__init__(self, master)
		self.master = master

		#Video Capture frame for both cameras
		self.frame = Label(self )
		self.frame.pack(side=LEFT)


		panelWidth = (master.winfo_width()-150)
		panelHeight = (master.winfo_height() -10)/2

		self.videoPanel1 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel1.pack(side=TOP)

		self.videoPanel2 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel2.pack(side=BOTTOM)

		def resizeVideoCapturePanels(videoPanel1, videoPanel2,controller):
			controller.updatePanels()
			panelWidth = (master.winfo_width()-150)
			panelHeight = (master.winfo_height() -10)/2

			videoPanel1.configure(width=panelWidth, height=panelHeight)
			videoPanel2.configure(width=panelWidth, height=panelHeight)
			controller.updatePanels()

		self.frame.bind("<Configure>", lambda e: resizeVideoCapturePanels(self.videoPanel1, self.videoPanel2, controller) )

		#Calibration tools
		calibrationLabel = Label(self, text="Calibration")
		calibrationLabel.pack(side=TOP)

		#Width
		onEditVar= StringVar()
		onEditVar.set(str(formParams['width']))
		onEditVar.trace("w", lambda name, index, mode, onEditVar=onEditVar: self.updateExportButton())
		vcmd = (master.register(self.validate),'%P', '%S')
		widthPanel = Label(self)
		widthLabel = Label(widthPanel, text="Width:")
		widthLabel.pack(side=LEFT)

		self.widthInput = Entry(widthPanel, width=11, validate = 'key', validatecommand = vcmd, textvariable=onEditVar)
		self.widthInput.pack(side=RIGHT)
		widthPanel.pack(side=TOP)


		#Height
		onEditVar= StringVar()
		onEditVar.set(str(formParams['height']))
		onEditVar.trace("w", lambda name, index, mode, onEditVar=onEditVar: self.updateExportButton())
		heightPanel = Label(self)
		heightLabel = Label(heightPanel, text="Height:")
		heightLabel.pack(side=LEFT)

		self.heightInput = Entry(heightPanel, width=11, validate = 'key', validatecommand = vcmd, textvariable=onEditVar)
		self.heightInput.pack(side=RIGHT)
		heightPanel.pack(side=TOP)

		#Units 
		unitsPanel = Label( self)
		calibrationLabel = Label(unitsPanel, text="Units:")
		calibrationLabel.pack(side=LEFT)

		self.unitsBox = ttk.Combobox(unitsPanel, width=10, state="readonly")
		self.unitsBox['values'] = ('centimeters', 'inches')
		self.unitsBox['state'] = 'readonly'
		self.unitsBox.set(formParams['units'])
		self.unitsBox.pack(side=RIGHT)
		unitsPanel.pack(side=TOP)

		#Export button
		self.exportButton = Button(self, text="Take photos and export", wraplength=80,  command=controller.exportClicked)
		self.exportButton.pack(side=BOTTOM)

	def validate(self,value,inputtext):
		'''Will only allow number to be inputed for entry widget used for width and height calibration
		'''
		if value is '':
		   return True
		if inputtext in '0123456789.':
			try:
				float(value)
				return True
			except ValueError:
				return False
		else:
			return False

	def updateExportButton(self):
		if self.heightInput.get() is '' or self.widthInput.get() is '':
			self.exportButton.configure( state=DISABLED)
		else :
			self.exportButton.configure( state=NORMAL)



class ExportViewController:
	def __init__(self, master, formParams={'width':0.0,'height':0.0,'units':'centimeters'}):
		self.master = master

		self.cam1 = cv2.VideoCapture(0)

		#Change this to one for now same cam
		self.cam2 = cv2.VideoCapture(0)
	
		self.view = ExportView(master, self, formParams)

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



	def exportClicked(self):
		'''Move to validation export view
		'''
		self.view.pack_forget()
		img1 = AppUtils.getImg(self.cam1)
		img2 = AppUtils.getImg(self.cam2)

		formParams ={'width':float(self.view.widthInput.get()),'height':float(self.view.heightInput.get()),'units':self.view.unitsBox.get()}
		from validationExportView import ValidationExportViewController
		ValidationExportViewController(self.master, formParams, img1, img2)


 
	def takePicture(self):
		''' Takes a picture from the current video capture
			saves the image under pictures directory as jpg 
			with the name current time in milliseconds since 
			epoch .jpg
		'''
		pictureName = str(int(time.time()))

		#Checking if pictures folder and creating, if it does not
		if not os.path.exists("pictures") :
				os.makedirs("pictures")

		for i in range(0, self.numOfCams):
			fullName = pictureName+ '_cam'+str(i)+  '.jpg'
			AppUtils.getImg(self.img_width_res,self.img_height_res, self.camList[i] ).save("pictures/" + fullName)
			print("Picture taken: " + fullName)
	