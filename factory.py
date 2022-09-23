
class Factory:
	def __init__(self):
		self.contents = []

	def add(self, tiles):
		self.contents = tiles

	def pop(self):
		contents = self.contents
		self.contents = []
		return contents