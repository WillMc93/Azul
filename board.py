import numpy as np

from floor_line import FloorLine
from tile import Tile
from pattern_line import PatternLine
from wall import Wall

class Board:
	# Define a player's board
	def __init__(self):
		self.score = 0
		self.wall = Wall()
		self.floor_line = FloorLine()
		self.pattern_lines = [PatternLine(i+1) for i in range(5)]


	def add_tiles(self, tiles, colour, line):
		# Add tiles to the pattern lines and return the runoff
		if tiles['first']:
			self.floor_line.add(tiles['first'].pop())

		# Pullout the wrong coloured tiles
		runoff = [tile for tile in tiles['tiles'] if tile.colour != colour]

		# Put the right coloured tiles into the pattern lines
		if self.pattern_lines[line].colour and self.pattern_lines[line].colour != colour:
			raise Exception("Programming Error: Trying to add wrong colour to pattern line.")
		tiles = [tile for tile in tiles['tiles'] if tile.colour == colour]
		floor = self.pattern_lines[line].add(tiles)
		
		# Put extra tiles on the floor
		self.floor_line.add(floor)
		return runoff


	def wall_tile(self):
		# Add tiles to the wall and clear pattern lines
		runoff = []
		for row, line in enumerate(self.pattern_lines):
			if pattern_line.full():
				tiles = line.clear()
				tile = tiles[0]
				if len(tiles) > 1:
					runoff.extend(tiles[1:])
				self.score += self.wall.add(tile, row)
		return runoff

