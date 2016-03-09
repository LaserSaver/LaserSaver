'''This class will contain all imports that the app needs as well as useful methods'''
from Tkinter import *
from mockModel import MockModel
import ttk
from PIL import Image, ImageTk
import cv2
import time
import os
from threading import Thread

class AppUtils: 
	@staticmethod
	def getImg(width, height, cam):
		'''   Getting an image object from the video capture

		'''
		ret, frame = cam.read()
		#Flipping horizontally 
		frame = cv2.flip(frame, 1)
		#Resizing to panel size
		frame = cv2.resize(frame, (width,height))
		cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		return Image.fromarray(cv2img)

	@staticmethod
	def computeOnSeprateThread(master, callback, function, kargs):
		thread = Thread(target = AppUtils.computationThread, args=[master, callback, function, kargs])
		#Starting seperate thread
		thread.start()

	@staticmethod
	def computationThread(master, callback, function, kargs):
		wentWell = function()

		#Performing call back on main thread
		master.after(0,callback(wentWell))