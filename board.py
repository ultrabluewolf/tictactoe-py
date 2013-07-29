"""Tic Tac Toe Board"""

class Board:
	MAX=3
	DGN=2
	CROSS='X'
	CIRC='O'
	BLANK='-'
	def __init__(self):
		self.board = []
		for i in range(MAX):
			self.board = []
	
	def __getitem__(self,i):
		return self.grid[i]
	def __setitem__(self,i,val):
		self.grid[i]=val
	
	def __str__(self):
		s = ''
		for row in range (Board.MAX):
			for col in range(Board.MAX):
				s += str(self.board[row][col])
				if col > 0 and col < Board.MAX-1:
					s += "|"
			s += "\n-----"
		return s
	