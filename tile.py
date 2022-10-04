from dataclasses import dataclass

@dataclass
class Tile:
	# A class defining the tiles, which is essentially just an
	# immutable string class with checks on the value of the string
	VALID_COLOURS = ('blue', 'yellow', 'red', 'black', 'white')
	__TILE_REPS = {'blue': '🟦', 'yellow': '🟨', 'red': '🟥', 'black': '⬛',
					'white': '⬜', 'first': '🏆', '': '❔'}
	colour: str = ''		

	def __init__(self, colour=''):
		# Make a Tile if a valid tile colour is provided
		if colour not in Tile.__TILE_REPS:
			raise Exception(f"Programming Error: Passed a non-valid label, {colour}, to a Tile object.")
		self.colour = colour


	def __eq__(self, other):
		# Definite equality between Tiles and Tiles or Tiles and strings
		if type(other) == str:
			return self.colour == other
		return self.colour == other.colour

	def __lt__(self, other)
		# Definte less_than for Tiles, which is used to sort Tiles by colour
		return self.colour < other.colour

	def __repr__(self):
		# Define the representation of Tile objects
		return f'Tile("{self.colour}")'


	def __str__(self):
		# Define the string representation of Tile objects
		return Tile.__TILE_REPS[self.colour]


	def set(self, colour):
		# Set the colour of a Tile if it is not already set, which is useful for
		# creating lists of unset tiles and setting them as necessary.
		# I think this might be unused
		if colour not in Tile.__TILE_REPS:
			raise Exception(f"Programming Error: Passed non-valid colour, {colour}, to Tile.set().")
		if self.colour != '':
			raise Exception(f"Programming Error: Trying to pass a new colour to a set tile.") 
		self.colour = colour
			