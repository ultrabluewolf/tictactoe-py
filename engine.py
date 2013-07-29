"""..."""

import board,player
from board import *
from player import *

class Engine:
	
	def __init__(self):
		self.board=Board()
		self.p1_score=0
		self.p2_score=0
	
	"""TODO"""
	def run_cli(self):
		print "Enter X or O: "
		