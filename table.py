from tile import Tile

class Table:
	def __init__(self):
		self.contents = self.__init_contents()


	def __init_contents(self):
		contents = {colour: [] for colour in Tile.VALID_COLOURS}
		contents = {'first': [Tile('first')]}
		return contents


	def add(self, tiles):
		if tile.colour not in Tile.VALID_COLOURS:
			raise Exception("Programming Error: Trying to add non-colour tile to Table.")

		for tile in self.contents:
			self.contents[tile.colour].append(tile)


	def take(self, colour, count):
		if colour not in Tile.VALID_COLOURS:
			raise Exception("Programming Error: Trying to pass invalid colour to Table.take()")
		if len(self.contents[colour]) < count:
			raise Exception("Programming Error: Trying to take too many tiles from table "
							f"(has {len(table.contents[colour])} {colour}s but {count} requested).")

		contents = [self.contents['first'].pop() for _ in self.contents['first'] if self.contents['first']]
		contents += [self.contents[colour].pop() for _ in range(count)]
		return contents


	def reset(self):
		if self.contents['first']:
			# Make sure the first tile is gone.
			self.contents['first'] = []
		contents = [*self.contents.values()]
		self.contents = self.__init_contents()
		return contents