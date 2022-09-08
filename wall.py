import copy

import numpy as np

from tile import Tile

# A Numpy Array with the first row of the wall pattern
# Pattern gets rolled to 
EMPTY_ROW = np.array([Tile(None) for _ in range(5)])
PATTERN_SEED = np.array([Tile('blue'), Tile('yellow'), Tile('red'),
						 Tile('black'), Tile('white')])

class Wall:
	# Class for containing a Wall. Checks validity and Scores itself
	def __init__(self):
		self.pattern = np.array([np.roll(copy.deepcopy(pattern_seed), i) 
								 for i in range(5)])
		self.filled = np.array([copy.deepcopy(EMPTY_ROW) for _ in range(5)])

	def add(tile, row):

		if tile in self.filled[row]:
			raise Exception("Programming Error: Filling a row with a known tile")

		else: 
