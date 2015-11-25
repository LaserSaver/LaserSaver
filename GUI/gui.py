#!/usr/bin/python
from Tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import os

class App:
	def __init__(self, master,cam):
		self.cam = cam
		self.master = master

		#Main Frame
		frame = LabelFrame(master,text='LazerCutter GUI')
		frame.pack()
		
		#Video Capture frame
		panel = Label(frame, width = 640, height= 480)
		panel.pack(side=TOP)
		self.panel = panel 
		self.update_panel()

		#Exit button
		self.exitButton = Button(frame, text="Exit", fg="red", command=master.destroy)
		self.exitButton.pack(side=RIGHT)

		#Take Picture button
		self.pictureButton = Button(frame, text="Take picture", command=self.take_picture)
		self.pictureButton.pack(side=LEFT)

	def getImg(self):
		#Getting img from video capture
		ret, frame = self.cam.read()
		#Flipping horizontally 
		frame = cv2.flip(frame, 1)
		#Resizing to panel size
		frame = cv2.resize(frame, (self.panel.winfo_width(),self.panel.winfo_height()))
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		return Image.fromarray(cv2img)

	def take_picture(self):
		#Saving picture to file
		pictureName = str(int(time.time())) + '.jpg'
		print("Picture taken: " + pictureName)

		#Checking if pictures folder and creating, if it does not
		if not os.path.exists("pictures") :
    			os.makedirs("pictures")

		self.getImg().save("pictures/" + pictureName)

	
		
	def update_panel(self):
		#Updating panel to current image from cam
		imgtk = ImageTk.PhotoImage(self.getImg())
		self.panel.configure(image = imgtk)
		self.panel.image = imgtk
		#Update capture every 10 milliseconds
		self.master.after(10, self.update_panel)



root = Tk()
cam = cv2.VideoCapture(0)
app = App(root,cam)
root.mainloop()
del cam