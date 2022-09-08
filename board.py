import numpy as np

from tile import Tile
from wall import Wall

class Board:

	# Define a player's board
	def __init__(self):
		self.points = 0
		self.pattern_lines = [np.zeros(i+1) for i in range(5)]
		self.wall = Wall()
