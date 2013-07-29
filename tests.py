#!/usr/bin/env python

"""..."""

import board,player,validator,utils
from board import *
from validator import *

print "some tests..."
boards = utils.read_input("input")

for i in range(len(boards)):
	print str(boards[i])
	print is_winner(boards[i])
	print "\n"
