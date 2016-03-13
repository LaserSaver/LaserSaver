from appUtils import *


class MainView(Frame):
	def __init__(self, master, controller):
		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		Frame.__init__(self, master)
		self.master = master

		self.max_panel_width = 600
		self.max_panel_height = 480

		#Main Frame
		self.frame = LabelFrame(master,text='Video Capture')
		self.frame.pack(side=LEFT)
		
		self.panelList = []
		
		self.toppanel = None
		self.bottompanel = None
		
		#Video Capture frames
		panel = Label( width = self.max_panel_width, height= self.max_panel_height)
		self.panelList.append( panel)
		panel.pack(in_=self.frame)

		panel2 = Label()
		self.panelList.append(panel2)

		panel3 = Label()
		self.panelList.append(panel3)

		panel4 = Label()
		self.panelList.append(panel4)

		#Calibration tools
		calibrationLabel = Label(master, text="Calibration")
		calibrationLabel.pack(side=TOP)


		#Cameras combo box
		camerasPanel = Label(master)
		camerasLabel = Label(camerasPanel, text="Cameras:")
		camerasLabel.pack(side=LEFT)
	
		self.camerasBox = ttk.Combobox(camerasPanel, width=10, state="readonly")
		self.camerasBox.bind("<<ComboboxSelected>>", controller.numberOfCamChange)
		self.camerasBox['values'] = ('1', '2', '3', '4')
		self.camerasBox.current(0)
		self.camerasBox.grid(column=0, row=0)
		self.camerasBox.pack(side=RIGHT)
		camerasPanel.pack(side=TOP)

		#Width
		vcmd = (master.register(self.validate),'%P', '%S')
		widthPanel = Label(master)
		widthLabel = Label(widthPanel, text="Width:")
		widthLabel.pack(side=LEFT)

		self.widthInput = Entry(widthPanel, width=11, validate = 'key', validatecommand = vcmd)
		self.widthInput.pack(side=RIGHT)
		widthPanel.pack(side=TOP)


		#Height
		heightPanel = Label(master)
		heightLabel = Label(heightPanel, text="Height:")
		heightLabel.pack(side=LEFT)

		self.heightInput = Entry(heightPanel, width=11, validate = 'key', validatecommand = vcmd)
		self.heightInput.pack(side=RIGHT)
		heightPanel.pack(side=TOP)

		#Units 
		unitsPanel = Label( master)
		calibrationLabel = Label(unitsPanel, text="Units:")
		calibrationLabel.pack(side=LEFT)

		self.unitsBox = ttk.Combobox(unitsPanel, width=10, state="readonly")
		self.unitsBox['values'] = ('centimeters', 'inches')
		self.unitsBox.current(0)
		self.unitsBox.grid(column=0, row=0)
		self.unitsBox.pack(side=RIGHT)
		unitsPanel.pack(side=TOP)

		#Exit button
		exitButton = Button(master, text="Exit", fg="red", command=master.destroy)
		exitButton.pack(side=BOTTOM)

		#Take Picture button
		pictureButton = Button(master, text="Take picture", command=controller.takePicture)
		pictureButton.pack(side=BOTTOM)

		#Export button
		exportButton = Button(master, text="Export", command=controller.export)
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

	def changeNumOfPanels(self, numOfPanels):
		''' Changing number of cameras and updating the GUI to accomdate
		'''
		#Removing all panels
		for i in range(0, 4):
			self.panelList[i].pack_forget()

		if self.view.toppanel is not None :
			self.toppanel.pack_forget()

		if self.view.bottompanel is not None :
			self.bottompanel.pack_forget()

		self.numOfCams = int(self.camerasBox.get()) 
		if numOfPanels == 1:
			self.panelList[0].configure(width=self.max_panel_width, height=self.max_panel_height )
			self.panelList[0].pack(in_=self.frame)
		elif numOfPanelss == 2:
			self.panelList[0].configure(width=self.max_panel_width/2, height=self.max_panel_height )
			self.panelList[0].pack(in_=self.frame,side=LEFT)

			self.panelList[1].configure(width=self.max_panel_width/2, height=self.max_panel_height )
			self.panelList[1].pack(in_=self.frame, side=RIGHT)
		elif numOfPanels == 3:
			self.toppanel = Label(self.frame)
			self.toppanel.pack(side=TOP)

			self.panelList[0].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[0].pack(in_=self.toppanel, side=LEFT)

			self.panelList[1].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[1].pack(in_=self.toppanel,side=RIGHT)

			self.panelList[2].configure(width=self.max_panel_width, height=self.max_panel_height/2 )
			self.panelList[2].pack(in_=self.frame,side=BOTTOM)
		elif numOfPanels == 4:
			self.toppanel = Label(self.frame)
			self.toppanel.pack(side=TOP)

			self.panelList[0].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[0].pack(in_=self.toppanel, side=LEFT)

			self.panelList[1].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[1].pack(in_=self.toppanel,side=RIGHT)

			self.bottompanel = Label(self.frame)
			self.bottompanel.pack(side=BOTTOM)

			self.panelList[2].configure(width=self.max_panel_width/2, height=(self.max_panel_height/2 ) )
			self.panelList[2].pack(in_=self.bottompanel, side=LEFT)

			self.panelList[3].configure(width=self.max_panel_width/2, height=(self.max_panel_height/2 ) )
			self.panelList[3].pack(in_=self.bottompanel,side=RIGHT)

class MainViewController:
	def __init__(self, master, model):

		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		self.img_width_res = 600
		self.img_height_res = 480

		self.master = master
		self.model = model

		self.numOfCams = 1

		self.camList = []
		self.camList.append(cv2.VideoCapture(0))
		self.camList.append(cv2.VideoCapture(1))
		self.camList.append(cv2.VideoCapture(2))
		self.camList.append(cv2.VideoCapture(3))

		self.view = MainView(master, self)

		self.updatePanel()
		self.view.pack()


	def updatePanel(self):
		''' Updates the image in the video capture 
			panel every 50 milliseconds
		'''
		for i in range(0, self.numOfCams):
			imgtk = ImageTk.PhotoImage(AppUtils.getImg(self.view.panelList[i].winfo_width(),self.view.panelList[i].winfo_height(),self.camList[i]))
			self.view.panelList[i].configure(image = imgtk)
			self.view.panelList[i].image = imgtk
		#Update capture every 50 milliseconds
		self.master.after(50, self.updatePanel)

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
	


	def numberOfCamChange(self, event):
		''' Changing number of cameras and updating the GUI to accomdate
		'''
		self.numOfCams = int(self.view.camerasBox.get()) 
		self.view.changeNumOfPanels(numOfCams)