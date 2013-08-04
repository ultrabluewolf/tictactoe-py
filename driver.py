#!/usr/bin/env python

"""..."""
import engine,player,argparse
from engine import *
from player import *

parser = argparse.ArgumentParser()
parser.add_argument('-c','--cli',action='store_false',help='commandline interface mode')
args = parser.parse_args()

game=Engine()
game.run(args.cli)
