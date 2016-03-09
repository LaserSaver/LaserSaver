from appUtils import *

class ContoursView(Frame):
	def __init__(self, master, controller):
		Frame.__init__(self, master)


class ContoursViewController:
	def __init__(self, master):
		self.master = master

		self.view = ContoursView(master, self)
		self.view.pack()