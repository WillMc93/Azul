from tile import Tile

class PatternLine:
	def __init__(self, max_size):
		self.max_size = max_size
		self.colour = None
		self.line = []


	def add(self, tiles, colour):
		# Add tiles to this pattern line and return the tiles that couldn't or shouldn't be added.
		if len(self.line) == self.max_size:
			raise Exception("Programming Error: Trying to add to a filled pattern line.")
		if colour not in Tile.VALID_COLOURS:
			raise Exception("Programming Error: Invalid colour passed to pattern line.")
		if self.colour != None and colour != self.colour:
			raise Exception("Programming Error: Trying to add wrong colour to pattern line.")

		# Set the colour of this line if necessary
		if self.colour == None:
			self.colour = colour

		# Add the tiles to the pattern but discard extras
		floor = []
		keep_len = self.max_size - len(self.line)
		self.line.extend(tiles[:keep_len])
		if len(tiles) > self.max_size - len(self.line):
			floor = tiles[keep_len:]
		return floor


	def full(self):
		# Checks if the pattern line is filled.
		return len(self.line) == self.max_size


	def clear(self):
		# Return the tiles from this pattern line and make it empty
		if self.size != self.max_size:
			raise("Programming Error: Trying to clear an incomplete pattern line.")
		tiles = self.line
		self.line = []
		self.colour = None
		return tiles
