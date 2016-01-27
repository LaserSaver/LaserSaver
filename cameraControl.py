import picamera
import RPi.GPIO as GPIO
import time
import os


def analyze_image(image):
   i = 0
   # Do stuff

def take_picture():
   camera = picamera.PiCamera()
   #Determine what brightness we should use.
   #If too dark, adjust the brightness
   newBrightness = 70
   camera.brightness = newBrightness
   camera.capture('image.jpg')
   #Probably do something to the image to make it readable by our computer vision code
   analyze_image(‘image.jpg’)

def detect_input():
   #adjust for where your switch is connected
   buttonPin = 17
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(buttonPin,GPIO.IN)

   prev_input = 0

   while True:
     #take a reading
     input = GPIO.input(buttonPin)
     #if the last reading was low and this one high, print
     if ((not prev_input) and input):
       take_picture()
     #update previous input
     prev_input = input
     #slight pause to prevent bouncing
     time.sleep(0.05)


def main():
   detect_input()

if __name__ == "__main__":
   main()
