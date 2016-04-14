from time import time
import os

class Camera:
	def __init__(self):
		cwd = os.getcwd()
		assets = os.path.join(cwd, 'assets')
		self.frames = [open(os.path.join(assets, f), 'rb').read() for f in os.listdir(assets)]

	def get_frame(self):
		return self.frames[int(time()) % 3]