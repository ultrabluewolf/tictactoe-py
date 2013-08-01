#!/usr/bin/env python

"""..."""

import board,player,engine,validator,utils
from board import *
from validator import *
from player import *
from engine import *

print "some tests..."
print "is_winner tests:"
boards = utils.read_input("input")
for i in range(len(boards)):
	print str(boards[i])
	print "w=" + is_winner(boards[i]) + "\n"

	
#--------------------------------------

print 'player.next_move tests:'
boards = utils.read_input("input-ai")
for i in range(len(boards)):
	p1=Player(Board.CROSS,Engine.P1,True)
	p2=Player(Board.CIRC,Engine.P2,True)
	turn=Board.CROSS
	print str(i+1) + '.'
	print str(boards[i]) + "\n"
	while not boards[i].is_full() and is_winner(boards[i]) == Board.BLANK:
		if turn == p1.sym:
			loc = p1.next_move(boards[i])
			boards[i][loc[0]][loc[1]] = p1.sym
		else:
			loc = p2.next_move(boards[i])
			boards[i][loc[0]][loc[1]] = p2.sym
		print str(boards[i]) + "\n"
		turn = get_opposite(turn)
		
	print "w=" + is_winner(boards[i]) + "\n"
