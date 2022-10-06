import arguments
from game import Game

def main_loop(game):
	# Play the game
	winner = None
	while not winner:

		game.fill_factories()
		
		for idx, player in enumerate(game.players):
			# Output the factory contents and table contents for this player
			for idx, factory in enumerate(game.factories):
				print(f"Factory {idx} has: {factory}")
			print(f"Table has: {game.table}")

			# Output the board state to standard error
			# write_err(self.board_state())

			move = input(f"{game.player} enter move: ")


if __name__ == '__main__':
	# Get command line arguments
	parser = arguments.init_parser()
	args = parser.parse_args()
	arguments.check_args(args)

	# Combine the lists of players and ai into a single list (TODO: Make this make sense, as opposed to just having a single pool of players and bots.)
	combine = args['players'].extend(args['ai'])
	game = Game(players=combine)
	main_loop(game)

