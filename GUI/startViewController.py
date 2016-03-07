from appUtils import *
from mainViewController import MainViewController

class StartViewController:
	def __init__(self, master, model):
		#Removing all widgets from previous view
		for child in master.winfo_children():
			child.destroy()

		self.master = master
		self.model = model

		calibrationLabel = Label(master, text="This is the Start View")
		calibrationLabel.pack(side=TOP)

		self.startButton = Button(master, text="Start", fg="red", command=self.start)
		self.startButton.pack(side=BOTTOM)

	def start(self):
		self.startButton.pack_forget()
		progressbar = ttk.Progressbar(orient=HORIZONTAL, length=100, mode='determinate')
		progressbar.pack(side=BOTTOM)
		progressbar.start()
		self.model.calculate(self.finish, self.master)

	def finish(self):
		MainViewController(self.master, self.model)
