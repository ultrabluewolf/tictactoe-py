"""..."""

import board,player,validator
from board import *
from validator import *
from player import *

class Engine:
	RESTART="restart"
	ROW=0
	COL=1
	P1='P1'
	P2='P2'
	def __init__(self):
		self.board=Board()
		self.p1=None
		self.p2=None
		self.p1_score=0
		self.p2_score=0
		self.turn=None
	
	"""TODO"""
	def run_cli(self):
		#game setup
		while True:
			"""TODO...cli input..."""
			print "How many human players? (0-2) "
			self.num_players=1
			print "Enter X or O for player1: "
			sym = "x"
			if self.num_players==1:
				self.p1=Player(sym,Engine.P1,True)
				self.p2=Player(get_opposite(sym),Engine.P2,False)
			elif self.num_players==2:
				self.p1=Player(sym,Engine.P1,False)
				self.p2=Player(get_opposite(sym),Engine.P2,False)
			else: #AI players
				self.p1=Player(sym,Engine.P1,True)
				self.p2=Player(get_opposite(sym),Engine.P2,True)
			
			if self.p1.sym == Board.CROSS:
				self.turn=Engine.P1
			else:
				self.turn=Engine.P2
			
			#gameplay
			while True:
				#TODO...read command line input...parse...
				Print "..."
				if self.num_players >= 1 and is_move(command):
					loc=get_move_loc(command)
					if self.turn == Engine.P1:
						self.board[loc[ROW]][loc[COL]] = self.p1.sym
					else
						self.board[loc[ROW]][loc[COL]] = self.p2.sym
					print self.board
					self.check_for_win()
				elif command==Engine.RESTART:
					self.restart()
					break
				elif command==Engine.STATUS:
					print self.status
				elif command==Engine.QUIT:
					return
				else: #ai player
					if self.turn == Engine.P1:
						loc=self.p1.next_move(self.board)
						self.board[loc[ROW]][loc[COL]] = self.p1.sym
					else:
						loc=self.p2.next_move(self.board)
						self.board[loc[ROW]][loc[COL]] = self.p2.sym
					print self.board
					self.check_for_win()
	
	"""TODO"""
	def run_gui(self):
		pass
	
	def restart(self):
		self=self__init__()
	
	def check_for_win(self):
		winner = self.board.is_winner()
		if not is_blank(winner):
			print winner
			if self.p1.sym == winner:
				self.p1_score+=1
			else:
				self.p2_score+=1
		if self.board.is_full():
			print "tied game"
			self.board.clear()
	
	def status(self):
		return "Scores:\n" + "p1: " + str(self.p1_score) + ", p2: " + str(self.p2_score)
		