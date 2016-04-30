from appUtils import *
from baseView import BaseView

class PromptSkewView(BaseView):
	def __init__(self, master, controller):
		''' Sets up The PromptSkewView 
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(PromptSkewController object): The controller which will be in charge of the view
		'''
		BaseView.__init__(self, master)

		self.addTitle("Skew Calibration")

		self.panel = Frame(self,relief=RIDGE, borderwidth=2)
		self.panel.pack_propagate(0) 
		self.panel.pack(side=TOP)

		scrollbar = Scrollbar(self.panel)
		scrollbar.pack(side=RIGHT, fill=Y)

		instructions = Text(self.panel,  wrap=WORD, yscrollcommand=scrollbar.set, state=NORMAL)
		instructions.delete(1.0, END)
		instructions.insert(END, "Skew Calibration Instructions: \nSkew calibration is not necessary to proceed. If you skip Skew Calibration, however, your results will be less accurate. \nStep 0: Press Calibrate button \nStep 1: Print out <location of circlegrid pattern> \nStep 2: Place printout on machine bed, with entire pattern in view of camera. \nStep 3: Take two(2) photos. \nStep 4: Rotate image in bed by ~ 15-20 degrees. \nStep 5: Take photo. \nStep 6: Repeat steps 4 and 5 until you have taken at least 15 photos. \nStep 7: Press Start")
		instructions.config(state=DISABLED)
		instructions.pack(side=TOP, fill=BOTH, expand=True)

		def resizePanel(panel):
			panelWidth = (master.winfo_width()-10)
			panelHeight = (master.winfo_height() -195)

			panel.configure(width=panelWidth, height=panelHeight)

		self.panel.bind("<Configure>", lambda e: resizePanel(self.panel) )


		scrollbar.config(command=instructions.yview)


		self.skipButton = Button(self, text="Skip skew", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)
		
		self.calibrateButton = Button(self, text="Calibrate skew", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)

		self.deleteButton = Button(self, text="Delete skew", command=controller.deleteClicked)
		self.deleteButton.pack(side=BOTTOM)

