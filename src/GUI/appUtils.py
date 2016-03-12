'''This class will contain all imports that the app needs as well as useful methods'''
from Tkinter import *
import ttk
from PIL import Image, ImageTk
import cv2
import time
import os
from threading import Thread

class AppUtils: 
	@staticmethod
	def getImg(cam, width=640, height=400):
		'''   Getting an image object from the video capture
			  Width and Height are optional and their default will
			  be used as the standard resolution we use for the photos

		'''
		ret, frame = cam.read()
		#Flipping horizontally 
		frame = cv2.flip(frame, 1)
		#Resizing to panel size
		frame = cv2.resize(frame, (width,height))
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		return cv2img

	@staticmethod
	def getTkinterImg(cam, width, height):
		return ImageTk.PhotoImage(Image.fromarray(AppUtils.getImg(cam,width,height)))

	@staticmethod
	def converImgToTkinterImg(img, width, height):
		return ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (width, height))))

	@staticmethod
	def computeOnSeprateThread(master, callback, function, args):
		thread = Thread(target = AppUtils.computationThread, args=[master, callback, function, args])
		#Starting seperate thread
		thread.start()

	@staticmethod
	def computationThread(master, callback, function, args):
		retVal = function(*args)

		#Performing call back on main thread
		master.after(0,callback, retVal)