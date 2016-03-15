from appUtils import *
from baseView import BaseView

class ScaleView(BaseView):
	def __init__(self, master, controller,formParams):
		''' 
		    Adding widgets:
			title, video capture, exit button, and take picture button

		'''
		BaseView.__init__(self, master)

		scaleLabel = Label(self, text="Scale calibration", font="-weight bold")
		scaleLabel.pack(side=TOP)


		#Video Capture frame for both cameras
		self.frame = Label(self )
		self.frame.pack(side=TOP)


		panelWidth = (master.winfo_width()-10)/2
		panelHeight = (master.winfo_height() -175)

		self.videoPanel1 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel1.pack(side=LEFT)

		self.videoPanel2 = Label(self.frame, width=panelWidth, height=panelHeight)
		self.videoPanel2.pack(side=RIGHT)

		def resizeVideoCapturePanels(videoPanel1, videoPanel2,controller):
			controller.updatePanels()
			panelWidth = (master.winfo_width()-10)/2
			panelHeight = (master.winfo_height() -175)

			videoPanel1.configure(width=panelWidth, height=panelHeight)
			videoPanel2.configure(width=panelWidth, height=panelHeight)
			controller.updatePanels()

		self.frame.bind("<Configure>", lambda e: resizeVideoCapturePanels(self.videoPanel1, self.videoPanel2, controller) )

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
		self.unitsBox['values'] = ('cm', 'in', 'mm')
		self.unitsBox['state'] = 'readonly'
		self.unitsBox.set(formParams['units'])
		self.unitsBox.pack(side=RIGHT)
		unitsPanel.pack(side=TOP)

		#Export button
		self.photosButton = Button(self, text="Take photos", wraplength=80,  command=controller.photosClicked)
		self.photosButton.pack(side=BOTTOM)

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
			self.photosButton.configure( state=DISABLED)
		else :
			self.photosButton.configure( state=NORMAL)

