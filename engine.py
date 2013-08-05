"""..."""

import pygame,sys,board,player,validator,cmd,re
#import pygame._view
from pygame.locals import *
from cmd import *
from board import *
from validator import *
from player import *

class Engine(cmd.Cmd):
	GFONT='/usr/share/fonts/truetype/msttcorefonts/arial.ttf'
	#GFONT='C:\Windows\Fonts\Arial.ttf'
	ROW=0
	COL=1
	P1='P1'
	P2='P2'
	COORD_RE=re.compile(
		'([1-' + str(Board.MAX) + ']),' 
			+ '([1-' + str(Board.MAX) + '])')
	
	def run(self,is_gui):
		self.is_gui = is_gui
		if is_gui:
			self.run_gui()
		else:
			self.run_cli()
	
	def run_cli(self):
		self.prompt="ttt>>>"
		self.cmdloop()
	
	"""TODO"""
	def run_gui(self):
		self.do_setup('')
	
		pygame.init()
		window=pygame.display.set_mode((350,350))
		pygame.display.set_caption('TicTacToe')
		
		dk_gray=pygame.Color(25,25,25)
		md_gray=pygame.Color(90,90,90)
		lt_gray=pygame.Color(190,190,190)
		red=pygame.Color(150,50,70)
		orange=pygame.Color(200,130,50)
		
		mfont = pygame.font.Font(Engine.GFONT,17)
		sfont = pygame.font.Font(Engine.GFONT,15)
		bfont = pygame.font.Font(Engine.GFONT,90)
		msg1 = '(0,0)'
		msg2 = '(0,0)'
		s_msg = '...'
		
		mouse_x, mouse_y = 0,0
		prev_hover = None
		prev_collide = None
		while True:
			window.fill(dk_gray)
			s_msg = self.status()
			
			msg_surf1 = mfont.render(msg1,True, md_gray)
			msg_surf2 = mfont.render(msg2,True, md_gray)
			s_msg_surf = sfont.render(s_msg,True, lt_gray)
			msg_rect1 = msg_surf1.get_rect()
			msg_rect2 = msg_surf2.get_rect()
			s_msg_rect = s_msg_surf.get_rect()
			msg_rect1.topleft = (10,window.get_height()-25)
			msg_rect2.topleft = (window.get_width()-75,window.get_height()-25)
			s_msg_rect.topleft = (10,10)
			window.blit(msg_surf1,msg_rect1)
			window.blit(msg_surf2,msg_rect2)
			window.blit(s_msg_surf,s_msg_rect)
			
			
			grid = []
			for row in range(Board.MAX):
				grid.append([])
				for col in range(Board.MAX):
					grid[row].append(pygame.Rect((55+row*90,45+col*90),(75,75)))
					if self.board[row][col] == 'X':
						grid_font = bfont.render(self.board[row][col],True, orange)
					elif self.board[row][col] == 'O':
						grid_font = bfont.render(self.board[row][col],True, red)
					elif self.gui_board[row][col] == 'X':
						grid_font = bfont.render(self.gui_board[row][col],True, md_gray)
					elif self.gui_board[row][col] == 'O':
						grid_font = bfont.render(self.gui_board[row][col],True, md_gray)
					else:
						grid_font = bfont.render('?',True, lt_gray)
					window.blit(grid_font,grid[row][col])
			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == MOUSEMOTION:
					mouse_x, mouse_y = event.pos
					msg1 = '('+str(mouse_x) + ',' + str(mouse_y)+')'
					
					# symbol hover -- on human player turns
					for row in range(Board.MAX):
						for col in range(Board.MAX):
							g_rect = grid[row][col]
							if (g_rect.collidepoint(mouse_x,mouse_y) 
									and prev_collide != g_rect and (
										(self.turn == Engine.P1 and not self.p1.is_ai) or (
											self.turn == Engine.P2 and not self.p2.is_ai))):
								if self.turn == Engine.P1:
									#grid_font = bfont.render(self.p1.sym,True, md_gray)
									self.gui_board[row][col] = self.p1.sym
								else:
									#grid_font = bfont.render(self.p2.sym,True, md_gray)
									self.gui_board[row][col] = self.p2.sym
								#window.blit(grid_font,grid[row][col])
								if prev_hover != None:
									self.gui_board[prev_hover[0]][prev_hover[1]] = (
											self.board[prev_hover[0]][prev_hover[1]])
								prev_hover = (row,col)
								prev_collide = g_rect
					
				elif event.type == MOUSEBUTTONUP:
					mouse_x, mouse_y = event.pos
					if event.button in (1,2,3):
						msg2 = '('+str(mouse_x) + ',' + str(mouse_y)+')'
						
						for row in range(Board.MAX):
							for col in range(Board.MAX):
								g_rect = grid[row][col]
								if (g_rect.collidepoint(mouse_x,mouse_y)):
									move_str = str(row+1) + ',' +str(col+1)
									self.do_move(move_str)
									#self.board[row][col] = 'X'
							
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.event.post(pygame.event.Event(QUIT))
			
			pygame.display.update()
	
	
	def check_for_win(self):
		winner = is_winner(self.board)
		if not is_blank(winner):
			print winner + " won!"
			self.board.clear()
			self.gui_board.clear()
			if self.p1.sym == winner:
				self.p1_score+=1
			else:
				self.p2_score+=1
		if self.board.is_full():
			print "tied game"
			self.board.clear()
			self.gui_board.clear()
	
	def status(self):
		if self.is_gui:
			return ("P1: " + str(self.p1_score) 
					+ "   P2: " + str(self.p2_score)
						+ "                                " 
							+ "Current Turn: " + str(self.turn))
		else:
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
		p1_move = self.p1.next_move(self.board)
		p2_move = self.p2.next_move(self.board)
		
		if self.num_players >= 1 and (
				(self.turn == Engine.P1 and p1_move == None) or 
					(self.turn == Engine.P2 and p2_move == None)):
			loc_strs=Engine.COORD_RE.findall(arg)[0]
			loc = []
			loc.append(int(loc_strs[Engine.ROW])-1)
			loc.append(int(loc_strs[Engine.COL])-1)
			
			if self.board.is_empty_spot(loc[Engine.ROW],loc[Engine.COL]):
				if self.turn == Engine.P1:
					self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					self.gui_board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					self.turn = Engine.P2
				else:
					self.board[loc[Engine.ROW]][loc[Engine.COL]] = self.p2.sym
					self.gui_board[loc[Engine.ROW]][loc[Engine.COL]] = self.p1.sym
					self.turn = Engine.P1
				self.check_for_win()
			else:
				print "invalid move"
			
		else: #ai player
			if self.turn == Engine.P1:
				#loc=self.p1.next_move(self.board)
				self.board[p1_move[Engine.ROW]][p1_move[Engine.COL]] = self.p1.sym
				self.gui_board[p1_move[Engine.ROW]][p1_move[Engine.COL]] = self.p1.sym
				
				self.turn = Engine.P2
			else:
				#loc=self.p2.next_move(self.board)
				self.board[p2_move[Engine.ROW]][p2_move[Engine.COL]] = self.p2.sym
				self.gui_board[p2_move[Engine.ROW]][p2_move[Engine.COL]] = self.p2.sym
				self.turn = Engine.P1
			#print self.board
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
		
		#gui prep.
		self.gui_board=Board()
		
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
			self.p1=Player(sym,Engine.P1,False)
			self.p2=Player(get_opposite(sym),Engine.P2,True)
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
		
		if (not self.is_gui):
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
		self.do_move(None)
