#Temporary class, this will be the class Zak will have to make, linking togther everyone else's classes
import time
from threading import Thread
class MockModel:

	def wait(self, callback, master):
		#Do your computation here on a seperate thread
		time.sleep(5)

		#After finishing computation it is important make sure to call
		#master.after 0 callback to make sure we execute
		#the callback back on the main GUI thread
		master.after(0,callback)

	def calculate(self, callback,master):
		thread = Thread(target = self.wait, args=[callback, master])
		#Starting seperate thread
		thread.start()

