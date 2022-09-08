class Tile:
	VALID_COLOURS = ['blue', 'yellow', 'red', 'black', 'white', '-1', None]

	def __init__(self, colour=None):
		if colour not in Tile.VALID_COLOURS:
			raise Exception(f"Programming Error: Passed a non-valid colour, {colour}, to a Tile object.")
		self.colour = colour

	def __eq__(self, tile):
		if tile.colour == None:
			raise Exception(f"Programming Error: Attempting to compare a filled tile to an empty one.")
		return self.colour == tile.colour

	def __repr__(self):
		return f'Tile("{self.colour}")'

	def __str__(self):
		out = None

		if self.colour == 'blue':
			out = '🟦'
		elif self.colour == 'yellow':
			out = '🟨'
		elif self.colour == 'red':
			out = '🟥'
		elif self.colour == 'black':
			out = '⬛'
		elif self.colour == 'white':
			out = '⬜'
		elif self.colout == '-1':
			out = '⛔'

		return out

	def set(self, colour):
		if colour not in Tile.VALID_COLOURS:
			raise Exception(f"Programming Error: Passed non-valid colour, {colour}, to Tile.set().")

		if self.colour == None:
			self.colour = colour
		else:
			raise Exception(f"Programming Error: Trying to pass a new colour to a set tile.") 
