from appUtils import *
from baseView import BaseView

class ExportView(BaseView):
	def __init__(self, master, controller, json):
		''' Sets up the export view 
		 
		    Args:
		    	master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	controller(ExportController object): The controller which will be in charge of the view
		    	jsonText(String): The json text which is displayed to the user after export
		'''
		BaseView.__init__(self, master)

		self.addTitle("JSON Exported")

		panel = Frame(self)
		panel.pack(side=TOP)

		scrollbar = Scrollbar(panel)
		scrollbar.pack(side=RIGHT, fill=Y)

		jsonText = Text(panel,  wrap=WORD, yscrollcommand=scrollbar.set, relief=RIDGE, borderwidth=2,state=NORMAL)
		jsonText.delete(1.0, END)
		jsonText.insert(END, json)
		jsonText.config(state=DISABLED)
		jsonText.pack(side=TOP)




		scrollbar.config(command=jsonText.yview)

		#Configure is for when window is resized 
		#jsonMes.bind("<Configure>", lambda e: jsonMes.configure(width=master.winfo_width()-50))


		self.skipButton = Button(self, text="Exit", command=master.destroy)
		self.skipButton.pack(side=BOTTOM)
