from appUtils import *
from exportView import ExportView


class ExportController:
	def __init__(self, master):
		self.master = master
		json = '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'
		self.view = ExportView(master, self ,json)
		self.view.pack(expand=YES,fill=BOTH)