from tile import Tile

class Factory:
	def __init__(self):
		self.contents = []

	def __str__(self):
		self.contents = sorted(self.contents)
		output = ' '.join(self.contents)
		output = output.strip()
		return output


	def add(self, tiles):
		# Store tiles in this factory
		if not all([tile.colour in Tile.VALID_COLOURS for tile in tiles]):
			raise Exception("Programming Error: Trying to pass non-colour tile to factory.")
		self.contents.extend(tiles)


	def pop(self):
		# Take the contents of the factory
		tiles = {'tiles': self.contents}
		tiles['first'] = None
		self.contents = []
		return tiles


	def is_empty(self):
		# Check to see if the factory is empty
		return not len(contents)