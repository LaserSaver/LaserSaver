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

		self.panel = Frame(self,relief=RIDGE, borderwidth=2)
		self.panel.pack_propagate(0) 
		self.panel.pack(side=TOP)

		scrollbar = Scrollbar(self.panel)
		scrollbar.pack(side=RIGHT, fill=Y)

		jsonText = Text(self.panel,  wrap=WORD, yscrollcommand=scrollbar.set, state=NORMAL)
		jsonText.delete(1.0, END)
		jsonText.insert(END, json)
		jsonText.config(state=DISABLED)
		jsonText.pack(side=TOP, fill=BOTH, expand=True)

		def resizePanel(panel):
			panelWidth = (master.winfo_width()-10)
			panelHeight = (master.winfo_height() -110)

			panel.configure(width=panelWidth, height=panelHeight)

		self.panel.bind("<Configure>", lambda e: resizePanel(self.panel) )


		scrollbar.config(command=jsonText.yview)



		self.skipButton = Button(self, text="Exit", command=master.destroy)
		self.skipButton.pack(side=BOTTOM)
