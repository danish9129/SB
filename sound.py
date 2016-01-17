import sound_lib
from sound_lib import output
from sound_lib import stream
o=output.Output()
class sound():
	handle=0
	def load(self,filename=""):
		self.handle =stream.FileStream(file=filename)
	def play(self):
		self.handle.looping=False
		self.handle.play()
	def play_looped(self):
		self.handle.looping=True
		self.handle.play()
	def stop(self):
		if not self.handle==0:
			self.handle.stop()
			self.handle.set_position(0)