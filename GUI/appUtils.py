'''This class will contain all imports that the app needs as well as useful methods'''
from Tkinter import *
from mockModel import MockModel
import ttk
from PIL import Image, ImageTk
import cv2
import time
import os

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