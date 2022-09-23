from random import randint

import numpy as np

from board import Board
from factory import Factory
from floor import Floor

class Game:
	FACTORIES = {2: 5, 3: 7, 4: 9}
	FILL_SIZE = 4

	def __init__(self, players):
		self.bag = [Tile(colour) * 20 for colour in Tile.VALID_COLOURS]
		self.boards = [Board() for _ in range(players)]
		self.factories = [Factory() for _ in range(FACTORIES[players])]
		self.floor = Floor()

	def fill_factories(self):
		for factory in self.factories:
			pieces = []
			for i in range(FILL_SIZE):
				idx = randint(len(self.bag))
				pieces.append(self.bag.pop(idx))
			factory.add(pieces)

	def game_status(self, player):
		# Make a numpy array of the current status of the game
		pass
