from appUtils import *
from homeController import HomeController

class BaseView(Frame):
	def __init__(self, master):
		''' The base view that most views will inheriet from in the application, adds a home button to
			go back to the home screen
		    
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		Frame.__init__(self, master)

		self.master = master
		self.homeButton = Button(self, text="Home", command=self.homeClicked)
		self.homeButton.pack(side=BOTTOM, anchor=W)

	def homeClicked(self):
		'''Home butaton is clicked unpacks the current view and pushes on the home view'''
		self.pack_forget()
		HomeController(self.master)