from appUtils import *


class ExportView(Frame):
	def __init__(self, master, controller):
		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		Frame.__init__(self, master)
		self.master = master

		#Video Capture frame for both cameras
		self.frame = LabelFrame(self,text='Video Capture')
		self.frame.pack(side=LEFT)
		
		panel = Label(self.frame, width = self.max_panel_width, height= self.max_panel_height)
		self.panelList.append( panel)
		panel.pack(side=LEFT)

		panel = Label(self.frame, width = self.max_panel_width, height= self.max_panel_height)
		self.panelList.append( panel)
		panel.pack(side=RIGHT)

		#Calibration tools
		calibrationLabel = Label(self, text="Calibration")
		calibrationLabel.pack(side=TOP)

		#Width
		vcmd = (master.register(self.validate),'%P', '%S')
		widthPanel = Label(self)
		widthLabel = Label(widthPanel, text="Width:")
		widthLabel.pack(side=LEFT)

		self.widthInput = Entry(widthPanel, width=11, validate = 'key', validatecommand = vcmd)
		self.widthInput.pack(side=RIGHT)
		widthPanel.pack(side=TOP)


		#Height
		heightPanel = Label(self)
		heightLabel = Label(heightPanel, text="Height:")
		heightLabel.pack(side=LEFT)

		self.heightInput = Entry(heightPanel, width=11, validate = 'key', validatecommand = vcmd)
		self.heightInput.pack(side=RIGHT)
		heightPanel.pack(side=TOP)

		#Units 
		unitsPanel = Label( self)
		calibrationLabel = Label(unitsPanel, text="Units:")
		calibrationLabel.pack(side=LEFT)

		self.unitsBox = ttk.Combobox(unitsPanel, width=10, state="readonly")
		self.unitsBox['values'] = ('centimeters', 'inches')
		self.unitsBox.current(0)
		self.unitsBox.grid(column=0, row=0)
		self.unitsBox.pack(side=RIGHT)
		unitsPanel.pack(side=TOP)

		#Exit button
		exitButton = Button(self, text="Exit", fg="red", command=master.destroy)
		exitButton.pack(side=BOTTOM)

		#Export button
		exportButton = Button(self, text="Export pictures", command=controller.export)
		exportButton.pack(side=BOTTOM)

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

class ExportViewController:
	def __init__(self, master):

		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		self.img_width_res = 600
		self.img_height_res = 480

		self.master = master

		self.numOfCams = 2

		self.camList = []
		self.camList.append(cv2.VideoCapture(0))

		#Change this to one for now same cam
		self.camList.append(cv2.VideoCapture(0))
	
		self.view = ExportView(master, self)

		self.updatePanels()
		self.view.pack()


	def continiousUpdatePanel(self):
		self.updatePanels()
		#Update capture every 50 milliseconds
		self.master.after(50, self.continiousUpdatePanel)

	def updatePanels(self):
		''' Updates the images in the video capture 
		'''
		for i in range(0, self.numOfCams):
			imgtk = ImageTk.PhotoImage(AppUtils.getImg(self.view.panelList[i].winfo_width(),self.view.panelList[i].winfo_height(),self.camList[i]))
			self.view.panelList[i].configure(image = imgtk)
			self.view.panelList[i].image = imgtk

	def export(self):
		'''Will export to json data, yet to be implemented
		'''

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
	