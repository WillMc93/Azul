from dataclasses import dataclass

@dataclass
class Tile:
	# A class defining the tiles, which is essentially just an
	# immutable string class with checks on the value of the string
	__COLOUR_REPS = {'blue': '🟦', 'yellow': '🟨', 'red': '🟥', 'black': '⬛',
						'white': '⬜', '-1': '⛔', '': '❔'}
	colour: str = ''		

	def __init__(self, colour=''):
		if colour not in Tile.__COLOUR_REPS:
			raise Exception(f"Programming Error: Passed a non-valid colour, {colour}, to a Tile object.")
		self.colour = colour

	def __eq__(self, tile):
		return self.colour == tile.colour

	def __repr__(self):
		return f'Tile("{self.colour}")'

	def __str__(self):
		return Tile.__COLOUR_REPS[self.colour]

	def set(self, colour):
		if colour not in Tile.__COLOUR_REPS:
			raise Exception(f"Programming Error: Passed non-valid colour, {colour}, to Tile.set().")
		if self.colour != '':
			raise Exception(f"Programming Error: Trying to pass a new colour to a set tile.") 
		self.colour = colour
			