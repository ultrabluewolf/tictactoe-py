"""..."""

import random,board
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
		return [0,0]
	