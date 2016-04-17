from appUtils import *
from baseView import BaseView

class ScaleView(BaseView):
	def __init__(self, master, controller,formParams):
		''' Sets up the ScaleView

		  Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ScaleController object): The controller which will be in charge of the view
		    	formParams(Dictionary): The current form params
		'''
		BaseView.__init__(self, master)

		scaleLabel = Label(self, text="Scale calibration", font="-weight bold")
		scaleLabel.pack(side=TOP)


		#Video Capture frame for both cameras
		self.videoPanel = Label(self )
		self.videoPanel.pack(side=TOP)


		panelWidth = (master.winfo_width()-10)
		panelHeight = (master.winfo_height() -215)

		def resizeVideoCapturePanel(videoPanel, controller):
			controller.updatePanel()
			panelWidth = (master.winfo_width()-10)
			panelHeight = (master.winfo_height() -215)

			videoPanel.configure(width=panelWidth, height=panelHeight)
			controller.updatePanel()

		self.videoPanel.bind("<Configure>", lambda e: resizeVideoCapturePanel(self.videoPanel, controller) )

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
		self.photosButton = Button(self, text="Take photo", wraplength=80,  command=controller.photosClicked)
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
		'''If the fields for width and height are empty the export button will be set to DISABLED
		'''
		if self.heightInput.get() is '' or self.widthInput.get() is '':
			self.photosButton.configure( state=DISABLED)
		else :
			self.photosButton.configure( state=NORMAL)

