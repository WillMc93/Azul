from board import Board
from factory import Factory
from floor import Floor

class Game:
	FACTORIES = {2: 5, 3: 7, 4: 9}

	def __init__(self, players):
		self.boards = [Board() for _ in range(players)]
		self.factories = [Factory() for _ in range(FACTORIES[players])]
		self.floor = Floor()
