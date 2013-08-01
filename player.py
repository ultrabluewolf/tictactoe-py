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
		if self._is_ai and not board.is_full():
			loc = None
			if False:
				loc = board.find_near_full(self.sym)
			elif False:
				loc = board.find_near_full(validator.get_opposite(self.sym))
			elif False:
				loc = [Board.MAX/2,Board.MAX/2]
			else:
				while True:
					loc = [self.rand.randint(0,Board.MAX-1),self.rand.randint(0,Board.MAX-1]
					if self.board.is_empty_spot(loc):
						break
		return loc
	