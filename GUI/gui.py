#!/usr/bin/python
from Tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import os

class App:
	def __init__(self, master,cam):
		''' Initializing GUI window

		    adding widgets:
		    title, video capture, exit button, and take picture button

		'''
		self.cam = cam
		self.master = master

		#Main Frame
		frame = LabelFrame(master,text='LazerCutter GUI')
		frame.pack()
		
		#Video Capture frame
		panel = Label(frame, width = 640, height= 480)
		panel.pack(side=TOP)
		self.panel = panel 
		self.updatePanel()

		#Exit button
		self.exitButton = Button(frame, text="Exit", fg="red", command=master.destroy)
		self.exitButton.pack(side=RIGHT)

		#Take Picture button
		self.pictureButton = Button(frame, text="Take picture", command=self.takePicture)
		self.pictureButton.pack(side=LEFT)

	def getImg(self):
		'''   Getting an image object from the video capture

		'''
		ret, frame = self.cam.read()
		#Flipping horizontally 
		frame = cv2.flip(frame, 1)
		#Resizing to panel size
		frame = cv2.resize(frame, (self.panel.winfo_width(),self.panel.winfo_height()))
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		return Image.fromarray(cv2img)

	def takePicture(self):
		''' Takes a picture from the current video capture
		    saves the image under pictures directory as jpg 
		    with the name current time in milliseconds since 
		    epoch .jpg
		'''
		pictureName = str(int(time.time())) + '.jpg'
		print("Picture taken: " + pictureName)

		#Checking if pictures folder and creating, if it does not
		if not os.path.exists("pictures") :
    			os.makedirs("pictures")

		self.getImg().save("pictures/" + pictureName)

	
		
	def updatePanel(self):
		''' Updates the image in the video capture 
			panel every 10 milliseconds
		'''
		imgtk = ImageTk.PhotoImage(self.getImg())
		self.panel.configure(image = imgtk)
		self.panel.image = imgtk
		#Update capture every 10 milliseconds
		self.master.after(10, self.updatePanel)



root = Tk()
cam = cv2.VideoCapture(0)
app = App(root,cam)
root.mainloop()
del cam
