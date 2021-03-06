"""..."""

import random,board,validator
from random import *
from board import *

class Player:
	
	def __init__(self,sym,label,is_ai):
		self.rand = Random()
		self.sym=sym
		self.is_ai=is_ai
		self.label=label

	"""TODO:examine board give next move"""
	def next_move(self,board):
		loc = None
		if self.is_ai and not board.is_full():
			loc1 = board.find_near_full(self.sym)
			loc2 = board.find_near_full(validator.get_opposite(self.sym))
			if loc1 != None:
				loc = loc1
			elif loc2 != None:
				loc = loc2
			elif board.is_empty_spot(Board.MAX/2,Board.MAX/2):
				loc = [Board.MAX/2,Board.MAX/2]
			else:
				empty_locs = board.find_empty_spots()
				loc = empty_locs[self.rand.randint(0,len(empty_locs)-1)]
				#while True:
					#TODO: faster to let board list empty spots and to pick one of these at random?
					#loc = [self.rand.randint(0,Board.MAX-1),self.rand.randint(0,Board.MAX-1]
					#if board.is_empty_spot(loc):
					#	break
		return loc
	