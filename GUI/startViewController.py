from appUtils import *
from mainViewController import MainViewController


class StartView(Frame):
	def __init__(self, master, controller):
		Frame.__init__(self, master)

		calibrationLabel = Label(self, text="This is the Start View")
		calibrationLabel.pack(side=TOP)

		self.startButton = Button(self, text="Start", fg="red", command=controller.start)
		self.startButton.pack(side=BOTTOM)
		
		panel = Label(self, width = 100, height= 35)
		panel.pack(side=TOP)


class StartViewController:
	def __init__(self, master, model):
		self.master = master
		self.model = model

		self.view = StartView(master, self)
		self.view.pack()


	def start(self):
		self.view.startButton.pack_forget()
		progressbar = ttk.Progressbar(self.view, orient=HORIZONTAL, length=500, mode='determinate')
		progressbar.pack(side=TOP)
		progressbar.start()
		self.model.calculate(self.finish, self.master)

	def finish(self):
		#Removing the current view
		self.view.pack_forget()
		MainViewController(self.master, self.model)
