from appUtils import *
from baseView import BaseView

class ExportView(BaseView):
	def __init__(self, master, controller, jsonText):
		''' Sets up the export view 
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ExportController object): The controller which will be in charge of the view
		    	jsonText(String): The json text which is displayed to the user after export
		'''
		BaseView.__init__(self, master)

		label = Label(self, text="Congrutlations, successfully exported JSON", font="-weight bold")
		label.pack(side=TOP)

		jsonMes = Message(self, text=jsonText, relief=RIDGE, borderwidth=2)
		jsonMes.pack(side=TOP)

		#Configure is for when window is resized 
		jsonMes.bind("<Configure>", lambda e: jsonMes.configure(width=master.winfo_width()-50))


		self.skipButton = Button(self, text="Exit", command=master.destroy)
		self.skipButton.pack(side=BOTTOM)
