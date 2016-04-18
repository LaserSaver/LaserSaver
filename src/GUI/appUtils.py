'''This class will contain all imports that the app needs as well as useful methods'''
from Tkinter import *
import ttk
from PIL import Image, ImageTk
import cv2
import time
import os
from threading import Thread
import tkFont

class AppUtils: 

	#Creating cam
	cam = None

	#Frame Per Millisecond, update rate of video capture
	framePerMillis = 50
	CV_CAP_PROP_FRAME_WIDTH  = 3
	CV_CAP_PROP_FRAME_HEIGHT = 4

	
	@staticmethod
	def getCam():
		'''Gets a singleton insatnce of camera 1'''
		if AppUtils.cam is None:
			AppUtils.cam = cv2.VideoCapture(0)
			AppUtils.cam.set(AppUtils.CV_CAP_PROP_FRAME_WIDTH,1920)
			AppUtils.cam.set(AppUtils.CV_CAP_PROP_FRAME_HEIGHT,1080)
		return AppUtils.cam

	@staticmethod
	def getImg(cam, width=1920, height=1080):
		''' Getting an image object from the video capture
			Width and Height are optional and their default will
			be used as the standard resolution we use for the photos

			Args:
				cam(videoCapture): The camera which the picture will be taken from
		    	width(int): The width resolution of the image in pixels width
		    	height(int): The height resolution of the image in pixels width
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
		''' Gets tkinter image from the camera these images can be displayed inside the GUI
			
			Args:
				cam(videoCapture): The camera which the picture will be taken from
		    	width(int): The width resolution of the image in pixels width
		    	height(int): The height resolution of the image in pixels width
		'''
		return ImageTk.PhotoImage(Image.fromarray(AppUtils.getImg(cam,width,height)))

	@staticmethod
	def converImgToTkinterImg(img, width=None, height=None):
		''' Converts a standard image to tkinter image and resized it
			
			Args:
				img(Image): The standrd image object
		    	width(int): The resize width resolution of the image in pixels width
		    	height(int): The resize height resolution of the image in pixels width
		'''
		if width == None or height == None:
			return ImageTk.PhotoImage(Image.fromarray(img))
		return ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (width, height))))

	@staticmethod
	def computeOnSeprateThread(master, callback, function, args):
		''' Computes a function on a sperate thread as to not distub the main thread
			and later on callsback on the main thread after the function finished
			
			Args:
				master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	callback(function): The function to callback on once the processing function is done
		    	function(function): The processing function which will be ran on a seperate thread
		    	args(list): the arguments that are passed to the computing function
		'''
		thread = Thread(target = AppUtils.computationThread, args=[master, callback, function, args])
		#Starting seperate thread
		thread.start()

	@staticmethod
	def computationThread(master, callback, function, args):
		'''The thread function computes the function outside the main GUI thread to prevent blocking

			Args:
				master(Tk object): The toplevel widget of Tk which is the main window of an application
		    	callback(function): The function to callback on once the processing function is done
		    	function(function): The processing function which will be ran on a seperate thread
		    	args(list): the arguments that are passed to the computing function
	
		'''
		retVal = function(*args)

		#Performing call back on main thread
		master.after(0,callback, retVal)