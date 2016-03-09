from appUtils import *

class SkewView(Frame):
	def __init__(self, master, controller):
		Frame.__init__(self, master)


class SkewViewController:
	def __init__(self, master):
		self.master = master

		self.view = SkewView(master, self)
		self.view.pack()