import copy
import pdb

import numpy as np

from tile import Tile

DIRECTIONS = ['up', 'down', 'left', 'right']
EMPTY_ROW = np.array([Tile() for _ in range(5)])
PATTERN_SEED = np.array([Tile('blue'), Tile('yellow'), Tile('red'),
						 Tile('black'), Tile('white')])

class Wall:
	# Class for containing a Wall. Checks validity and Scores itself
	PATTERN = np.array([np.roll(copy.deepcopy(PATTERN_SEED), i) for i in range(5)])

	def __init__(self):
		self.tiled = np.array([copy.deepcopy(EMPTY_ROW) for _ in range(5)])


	def add(self, tile, row):
		# Function for adding a tile to self.tiled
		if tile in self.tiled[row]:
			raise Exception("Programming Error: Filling a row with a used tile")
		
		col = np.where(Wall.PATTERN[row] == tile)
		if len(col) == 1 and len(col[0]) == 1:
			col = col[0][0]
		else:
			raise Exception("Programming Error: np.where returned more than one index.")
		self.tiled[row][col] = tile
		score = self.add_score(row, col)
		return score


	def __add_score(self, row, col, direction):
		# Function for adding the scores up in one direction from the starting row/col.

		# Guard clause for me
		if direction not in DIRECTIONS:
			raise Exception(f"Programming Error: Direction, {direction}, is not valid.")

		# Initialize the orientation of the function
		if direction in ['up', 'left']:
			movement = lambda x: x - 1
			bounds = lambda x: x >= 0
		elif direction in ['down', 'right']:
			movement = lambda x: x + 1
			bounds = lambda x: x < 5
		orientation = 'col' if direction in ['up', 'down'] else 'row'

		# Internal function for moving our 'gaze' to the next tile
		def make_move(row, col):
			if orientation == 'col':
				return row, movement(col)
			else:
				return movement(row), col

		# Calculate the score
		score = 0
		_row, _col = make_move(row, col)
		while bounds(_row) and bounds(_col):
			if self.tiled[_row][_col] != Tile():
				score += 1
			else:
				break
			_row, _col = make_move(_row, _col)
		return score


	def add_score(self, row, col):
		# Function for getting the scores after each tile addition to self.tiled
		score = 1 # We get one point for putting a tile anywhere
		directions = ['up', 'down', 'left', 'right']
		for direc in directions:
			score += self.__add_score(row, col, direc)
		return score


	def end_score(self):
		# Calculate the bonus scores at the end of the game.
		score = 0 
		blank = Tile()

		# Internal function for cutting down on repeated code
		def award(count, reward):
			if count == 5:
				return reward
			return 0

		# Check for completed rows
		for row in range(5):
			count = np.count(self.tiled[row] != blank)
			score += award(count, 2)
		# Check for completed columns
		for col in range(5):
			count = np.count(self.tiled[:][col] != blank)
			score += award(count, 7)
		# Check for completed sets
		for colour in Tile.VALID_COLOURS:
			count = np.count(self.tiled == Tile(colour))
			score += award(count, 10)

		return score
