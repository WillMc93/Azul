from tile import Tile

class Table:
	def __init__(self):
		self.contents = self.__init_contents()

	def __str__(self):
		# Return the string representation of the table
		# TODO: TEST because I have no idea if this is going to work like I want it to
		output = ' '.join(self.contents['first']) if self.contents['first'] else ''
		for colour in Tile.VALID_COLOURS:
			output += ' '.join(self.contents[colour])
		return output


	def __init_contents(self):
		# Function for reinitializing the table contents 
		contents = {colour: [] for colour in Tile.VALID_COLOURS}
		contents = {'first': [Tile('first')]}
		return contents


	def add(self, tiles):
		# Add tiles to the table
		if tile.colour not in Tile.VALID_COLOURS:
			raise Exception("Programming Error: Trying to add non-colour tile to Table.")

		for tile in self.contents:
			self.contents[tile.colour].append(tile)


	def take(self, colour, count):
		# Take tiles from the table
		if colour not in Tile.VALID_COLOURS:
			raise Exception("Programming Error: Trying to pass invalid colour to Table.take()")
		if len(self.contents[colour]) < count:
			raise Exception("Programming Error: Trying to take too many tiles from table "
							f"(has {len(table.contents[colour])} {colour}s but {count} requested).")

		tiles = {}
		tiles['first'] = self.contents['first'].pop() if self.contents['first'] else None
		tiles['tiles'] = [self.contents[colour].pop() for _ in range(count)]
		return tiles


	def reset(self):
		# Reset the table to only contain the first tile returning the contents for the bag
		if self.contents['first']:
			# Make sure the first tile is gone.
			self.contents['first'] = []
		tiles = [*self.contents.values()]
		self.contents = self.__init_contents()
		return tiles