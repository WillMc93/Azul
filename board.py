import numpy as np

from floor_line import FloorLine
from tile import Tile
from pattern_lines import PatternLines
from wall import Wall

class Board:
	# Define a player's board
	def __init__(self):
		self.points = 0
		self.pattern_lines = PatternLines()
		self.wall = Wall()
		self.floor_line = FloorLine()
