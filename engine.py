"""..."""

import board,player,validator,cmd,re
from cmd import *
from board import *
from validator import *
from player import *

class Engine(cmd.Cmd):
	ROW=0
	COL=1
	P1='P1'
	P2='P2'
	COORD_RE=re.compile(
		'([1-' + str(Board.MAX) + ']),' 
			+ '([1-' + str(Board.MAX) + '])')
	
	def run_cli(self):
		self.prompt="ttt>>>"
		self.cmdloop()
	
	"""TODO"""
	def run_gui(self):
		pass
	
	def check_for_win(self):
		winner = is_winner(self.board)
		if not is_blank(winner):
			print winner + " won!"
			self.board.clear()
			if self.p1.sym == winner:
				self.p1_score+=1
			else:
				self.p2_score+=1
		if self.board.is_full():
			print "tied game"
			self.board.clear()
	
	def status(self):
		return ("Scores:\n" 
			+ "p1: " + str(self.p1_score) 
				+ ", p2: " + str(self.p2_score))
	
	def do_quit(self,arg):
		"""Quits the game"""
		print 'exiting game'
		return True
	
	def do_status(self,arg):
		"""Show current game status"""
		print self.status()
	
	def do_move(self,arg):
		"""Play next move on board - x,y"""
		#print 'playing move - ' + arg
		if self.num_players >= 1:
			loc_strs=Engine.COORD_RE.findall(arg)[0]
			loc = []
			loc.append(int(loc_strs[Engine.ROW])-1)
			loc.append(int(loc_strs[Engine.COL])-1)
			
			if self.board.is_empty_spot(loc[Engine.ROW],loc[Engine.COL]):
				if self.turn == Engine.P1:
					self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					self.turn = Engine.P2
				else:
					self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p2.sym
					self.turn = Engine.P1
				self.check_for_win()
			else:
				print "invalid move"
			
		else: #ai player
			if self.turn == Engine.P1:
				loc=self.p1.next_move(self.board)
				self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
			else:
				loc=self.p2.next_move(self.board)
				self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p2.sym
			print self.board
			self.check_for_win()
	
	def do_restart(self,arg):
		"""Restart the game (setup)"""
		self.do_setup(arg)
	
	def do_setup(self,arg):
		"""Setup game; defaults: P1 vs AI, with P1 as X"""
		self.p1=None
		self.p2=None
		self.board=Board()
		self.p1_score=0
		self.p2_score=0
		self.turn=None
		
		print "How many human players? (0-2):",
		input=raw_input()
		try:
			self.num_players = int(input)
			if self.num_players < 0 or self.num_players > 2:
				self.num_players = 1
		except ValueError:
			self.num_players=1
			
		print "Enter X or O for player1:",
		sym = raw_input().upper()
		if not is_cross(sym) or not is_circ(sym):
			sym = Board.CROSS
		
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
		
		print self.board
	
	
#	def precmd(self,line):
#		print "...pre"
#		return line
	
	def postcmd(self,stop,line):
		if not stop:
			print self.board
		return stop
	
	def preloop(self):
		"""game setup"""
		self.do_setup("")
	
	def postloop(self):
		"""print final game status"""
		print self.status()
	
	def emptyline(self):
		"""continue game"""
		pass
