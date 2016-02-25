#!/usr/bin/python
from Tkinter import *
import ttk
from PIL import Image, ImageTk
import cv2
import time
import os

class App:
	def __init__(self, master):
		''' Initializing GUI window

			adding widgets:
			title, video capture, exit button, and take picture button

		'''
		self.master = master

		self.camList = []
		self.camList.append(cv2.VideoCapture(0))
		self.camList.append(cv2.VideoCapture(1))
		self.camList.append(cv2.VideoCapture(2))
		self.camList.append(cv2.VideoCapture(3))

		self.max_panel_width = 600
		self.max_panel_height = 480

		#Main Frame
		self.frame = LabelFrame(master,text='LazerCutter GUI')
		self.frame.pack(side=LEFT)


		self.numOfCams = 1
		
		self.panelList = []
		
		self.toppanel = None
		self.bottompanel = None
		#Video Capture frames
		panel = Label( width = self.max_panel_width, height= self.max_panel_height)
		self.panelList.append( panel)
		self.updatePanel()
		panel.pack(in_=self.frame)

		panel2 = Label()
		self.panelList.append(panel2)

		panel3 = Label()
		self.panelList.append(panel3)

		panel4 = Label()
		self.panelList.append(panel4)


		#Take Picture button
		pictureButton = Button(master, text="Take picture", command=self.takePicture)
		pictureButton.pack(side=TOP)

		#Cameras combo box
		cameraLabel = Label(text="Cameras")
		cameraLabel.pack(side=TOP)
		self.box = ttk.Combobox(master, width=10)
		self.box.bind("<<ComboboxSelected>>", self.numberOfCamChange)
		self.box['values'] = ('1', '2', '3', '4')
		self.box.current(0)
		self.box.grid(column=0, row=0)
		self.box.pack(side=TOP)

		#Exit button
		exitButton = Button(master, text="Exit", fg="red", command=master.destroy)
		exitButton.pack(side=BOTTOM)


	def getImg(self, width, height, cam):
		'''   Getting an image object from the video capture

		'''
		ret, frame = cam.read()
		#Flipping horizontally 
		frame = cv2.flip(frame, 1)
		#Resizing to panel size
		frame = cv2.resize(frame, (width,height))
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		return Image.fromarray(cv2img)

	def takePicture(self):
		''' Takes a picture from the current video capture
			saves the image under pictures directory as jpg 
			with the name current time in milliseconds since 
			epoch .jpg
		'''
		pictureName = str(int(time.time()))

		#Checking if pictures folder and creating, if it does not
		if not os.path.exists("pictures") :
				os.makedirs("pictures")

		for i in range(0, self.numOfCams):
			fullName = pictureName+ '_cam'+str(i)+  '.jpg'
			self.getImg(self.max_panel_width,self.max_panel_height, self.camList[i] ).save("pictures/" + fullName)
			print("Picture taken: " + fullName)

	
		
	def updatePanel(self):
		''' Updates the image in the video capture 
			panel every 50 milliseconds
		'''
		for i in range(0, self.numOfCams):
			imgtk = ImageTk.PhotoImage(self.getImg(self.panelList[i].winfo_width(),self.panelList[i].winfo_height(),self.camList[i]))
			self.panelList[i].configure(image = imgtk)
			self.panelList[i].image = imgtk
		#Update capture every 50 milliseconds
		self.master.after(50, self.updatePanel)

	def numberOfCamChange(self, event):
		''' Changing number of cameras and updating the GUI to accomdate
		'''
		#Removing all panels
		for i in range(0, 4):
			self.panelList[i].pack_forget()

		if self.toppanel is not None :
			self.toppanel.pack_forget()

		if self.bottompanel is not None :
			self.bottompanel.pack_forget()

		self.numOfCams = int(self.box.get()) 
		if self.numOfCams == 1:
			self.panelList[0].configure(width=self.max_panel_width, height=self.max_panel_height )
			self.panelList[0].pack(in_=self.frame)
		elif self.numOfCams == 2:
			self.panelList[0].configure(width=self.max_panel_width/2, height=self.max_panel_height )
			self.panelList[0].pack(in_=self.frame,side=LEFT)

			self.panelList[1].configure(width=self.max_panel_width/2, height=self.max_panel_height )
			self.panelList[1].pack(in_=self.frame, side=RIGHT)
		elif self.numOfCams == 3:
			self.toppanel = Label(self.frame)
			self.toppanel.pack(side=TOP)

			self.panelList[0].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[0].pack(in_=self.toppanel, side=LEFT)

			self.panelList[1].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[1].pack(in_=self.toppanel,side=RIGHT)

			self.panelList[2].configure(width=self.max_panel_width, height=self.max_panel_height/2 )
			self.panelList[2].pack(in_=self.frame,side=BOTTOM)
		elif self.numOfCams == 4:
			self.toppanel = Label(self.frame)
			self.toppanel.pack(side=TOP)

			self.panelList[0].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[0].pack(in_=self.toppanel, side=LEFT)

			self.panelList[1].configure( width=self.max_panel_width/2, height=self.max_panel_height/2 )
			self.panelList[1].pack(in_=self.toppanel,side=RIGHT)

			self.bottompanel = Label(self.frame)
			self.bottompanel.pack(side=BOTTOM)

			self.panelList[2].configure(width=self.max_panel_width/2, height=(self.max_panel_height/2 ) )
			self.panelList[2].pack(in_=self.bottompanel, side=LEFT)

			self.panelList[3].configure(width=self.max_panel_width/2, height=(self.max_panel_height/2 ) )
			self.panelList[3].pack(in_=self.bottompanel,side=RIGHT)




root = Tk()
app = App(root)
root.mainloop()
