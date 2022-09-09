from itertools import product

import numpy as np

from tile import Tile

class FloorLine:
	PENALTIES = (-1, -1, -2, -2, -2, -3, -3)

	def __init__(self):
		self.line = []
		self.reset_line()

	def add(self, tile: Tile):
		# Add tile to the floor line
		if len(self.line) >= 7:
			raise Exception("Uhhh, the floor line exceeded the maximum.")
		self.line.append(tile)

	def score(self):
		# Calculate the score for this floor line
		score = 0
		for penalty, tile in product(PENALTIES, self.line):
			if tile != Tile():
				score += penalty
			else:
				break
		return score

	def reset_line(self):
		# Reset the floor line returning the tiles for recycle
		tiles = []
		for tile in self.line:
			if tile != Tile():
				tiles.append(tile)
		self.line = [Tile() for _ in range(7)]
		return tiles


	def as_ndarray(self):
		# Produce a np.array of this floor line.
		return np.array(self.line)


	

