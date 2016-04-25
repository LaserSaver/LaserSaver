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

		instructions = Message(self, text="Skew Calibration Instructions: \nSkew calibration is not necessary to proceed. If you skip Skew Calibration, however, your results will be less accurate. \nStep 0: Press Calibrate button \nStep 1: Print out <location of circlegrid pattern> \nStep 2: Place printout on machine bed, with entire pattern in view of camera. \nStep 3: Take two(2) photos. \nStep 4: Rotate image in bed by ~ 15-20 degrees. \nStep 5: Take photo. \n Step 6: Repeat steps 4 and 5 until you have taken at least 15 photos. \nStep 7: Press Start", relief=RIDGE, borderwidth=2)
		instructions.pack(side=TOP)

		#Configure is for when window is resized 
		instructions.bind("<Configure>", lambda e: instructions.configure(width=master.winfo_width()-50))


		self.skipButton = Button(self, text="Skip skew", command=controller.skipClicked)
		self.skipButton.pack(side=BOTTOM)
		
		self.calibrateButton = Button(self, text="Calibrate skew", command=controller.calibrateClicked)
		self.calibrateButton.pack(side=BOTTOM)

		self.deleteButton = Button(self, text="Delete skew", command=controller.deleteClicked)
		self.deleteButton.pack(side=BOTTOM)

