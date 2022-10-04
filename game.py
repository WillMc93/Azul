import argparse
import sys
from random import randint

import numpy as np

from board import Board
from factory import Factory
from floor import Floor

class Game:
	FACTORIES = {2: 5, 3: 7, 4: 9}
	FILL_SIZE = 4

	def __init__(self, players: list):
		self.num_players = len(players)
		self.players = players

		self.bag = [Tile(colour) * 20 for colour in Tile.VALID_COLOURS]
		self.boards = [Board() for _ in range(num_players)]
		self.factories = [Factory() for _ in range(FACTORIES[num_players])]
		self.table = Table()


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

	def move(self, board, board_line, source, colour, num=0):
		pass

	def main_loop(self, starting_player=0):
		# Play the game
		winner = None
		while not winner:

			for idx, player in enumerate(players):
				# Output the factory contents and table contents for this player
				for idx, factory in enumerate(self.factories):
					print(f"Factory {idx} has: {factory}")
				print(f"Table has: {self.table}")

				# Output the board state to standard error
				# write_err(self.board_state())

				move = input(f"Player {idx} enter move: ")


if __name__ == '__main__':


