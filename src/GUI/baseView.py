from appUtils import *
from homeController import HomeController

class BaseView(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		self.master = master
		self.homeButton = Button(self, text="Home", command=self.homeClicked)
		self.homeButton.pack(side=BOTTOM, anchor=W)

	def homeClicked(self):
		self.pack_forget()
		HomeController(self.master)