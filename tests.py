#!/usr/bin/env python

"""..."""

import board,player,validator,utils
from board import *
from validator import *

print "some tests..."
print "is_winner tests:"
boards = utils.read_input("input")
for i in range(len(boards)):
	print str(boards[i])
	print "w=" + is_winner(boards[i]) + "\n"
