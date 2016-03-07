#!/usr/bin/python
from appUtils import *
from startViewController import StartViewController

class App:
	def __init__(self, master):
		''' Initializing GUI window

		    Setting the viewController to start view

		'''

		from startViewController import StartViewController
		StartViewController(master, MockModel())


root = Tk()
root.wm_title("LazerCutter GUI")
app = App(root)
root.mainloop()
