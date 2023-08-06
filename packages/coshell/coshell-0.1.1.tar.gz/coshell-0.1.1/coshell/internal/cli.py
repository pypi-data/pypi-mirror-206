from argparse import ArgumentParser

# create the parser
parser = ArgumentParser(description='coshell')

# add arguments
parser.add_argument('text', type=str,
                    help='testing')

# parse the arguments
args = parser.parse_args()
