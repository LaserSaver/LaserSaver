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
		self.topFrame = Frame(self)
		self.homeButton = Button(self.topFrame, text="Home", command=self.homeClicked)
		self.homeButton.pack(side=LEFT)
		self.topFrame.pack(side=TOP,fill=X)

	def homeClicked(self):
		'''Home butaton is clicked unpacks the current view and pushes on the home view'''
		self.destroy()
		HomeController(self.master)

	def addTitle(self, title):
		'''Gives a way to set the title for all other inheriting views

			Args:
				title(string): the string of the title
		'''
		helv24 = tkFont.Font(family='Helvetica',size=24, weight='bold') 
		self.titleLabel = Label(self.topFrame, text=title, font="-weight bold", pady=5 )
		self.titleLabel['font'] = helv24
		self.titleLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


