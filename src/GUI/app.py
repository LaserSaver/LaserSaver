#!/usr/bin/python
from appUtils import *
from homeController import HomeController

class App:
	def __init__(self, master):

		''' Setting the viewController to HomeViewController
		    
		    Args:
		    	master(Tk object): The top level widget of Tk which is the main window of an application
		'''
		HomeController(master)


root = Tk()
root.wm_title("LazerCutter GUI")
root.geometry('{}x{}'.format(400, 400))
root.minsize(200, 200)
app = App(root)
root.mainloop()