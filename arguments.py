import argparse

def init_parser():
	# Function that defines the parser
	parser = argparse.ArgumentParser(description="Command Line Interface for Azul Game")
	parser.add_argument('--players', type=str, required=False, nargs='+',
							metavar='name', help="A list of up to four human players.")
	parser.add_argument('--ai', type=str, required=False, nargs='+',
							metavar='name', help="A list of up to four ai players.")
	return parser


def check_args(args):
	args = vars(args)
	players = args['players']
	bots = args['ai']

	if not players and not bots:
		raise Exception("No players or bots were defined.")

	elif players and bots:
		combined = len(args['players']) + len(args['ai'])
		if combined > 4:
			raise Exception(f"Too many players and bots. Can only have 4 combined at most."
								f"You gave {len(args['players'])} + {len(args['ai'])} = {combined}.")
	elif players and len(players) > 4:
		raise Exception(f"Too many players. Can only have 4 at most. You gave {len(args['players'])}.")
	elif bots and len(args['ai']) > 4:
		raise Exception(f"Too many bots. Can only have 4 at most. You gave {len(args['ai'])}.")
	else:
		raise Exception(f"No players or bots defined. Must define players or bots.")

	return True