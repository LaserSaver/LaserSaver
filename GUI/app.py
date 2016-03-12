#!/usr/bin/python
from appUtils import *
from promptSkewView import PromptSkewViewController

class App:
	def __init__(self, master):
		''' Initializing GUI window
		    Setting the viewController to promptSkewView 
		'''
		PromptSkewViewController(master)


root = Tk()
root.wm_title("LazerCutter GUI")
root.geometry('{}x{}'.format(400, 400))
root.minsize(200, 200)
app = App(root)
root.mainloop()