"""..."""

import board,player,validator,cmd
from cmd import *
from board import *
from validator import *
from player import *

class Engine(cmd.Cmd):
	RESTART="restart"
	STATUS="status"
	QUIT="quit"
	ROW=0
	COL=1
	P1='P1'
	P2='P2'
		
	"""TODO"""
	def run_cli(self):
		self.prompt="ttt>>>"
		self.cmdloop()
		
		#game setup
		while False:
					
			#gameplay
			while False:
				#TODO...read command line input...parse...
				print "..."
				command="\n"
				if self.num_players >= 1 and is_move(command):
					loc=get_move_loc(command)
					if self.turn == Engine.P1:
						self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					else:
						self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p2.sym
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
						self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					else:
						loc=self.p2.next_move(self.board)
						self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p2.sym
					print self.board
					self.check_for_win()
	
	"""TODO"""
	def run_gui(self):
		pass
	
	def check_for_win(self):
		winner = is_winner(self.board)
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
	
	def do_quit(self,arg):
		"""Quits the game"""
		print 'exiting game'
		return True
	
	def do_status(self,arg):
		"""Show current game status"""
		print 'status'
	
	def do_move(self,arg):
		"""Next move on board - x,y"""
		print 'playing move - ' + arg
	
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
		
		print "How many human players? (0-2) "
		input=raw_input()
		try:
			self.num_players = int(input)
			if self.num_players < 0 or self.num_players > 2:
				self.num_players = 1
		except ValueError:
			self.num_players=1
			
		print "Enter X or O for player1: "
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
	
	
	def precmd(self,line):
		print "...pre"
		return line
	
	def postcmd(self,stop,line):
		print "...post"
		return stop
	
	def preloop(self):
		"""game setup"""
		self.do_setup("")
	
	def postloop(self):
		"""print final game status"""
		print "...the score"
	
	def emptyline(self):
		"""continue game"""
		pass
