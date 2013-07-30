"""Tic Tac Toe Board"""

class Board:
	MAX=3
	DGN=2
	CROSS='X'
	CIRC='O'
	BLANK='-'
	
	def __init__(self):
		self.board = []
		for row in range(Board.MAX):
			self.board.append([])
			for col in range(Board.MAX):
				self.board[row].append(Board.BLANK)
	
	def replace(self,arr):
		for row in range(Board.MAX):
			for col in range(Board.MAX):
				self.board[row][col] = arr[row][col]
	
	def clear(self):
		self.board = []
		for row in range(Board.MAX):
			self.board.append([])
			for col in range(Board.MAX):
				self.board[row].append(Board.BLANK)
	
	def is_full(self):
		for row in range(Board.MAX):
			for col in range(Board.MAX):
				if board[row][col]==Board.BLANK:
					return False
		return True
	
	def __getitem__(self,i):
		return self.board[i]
	def __setitem__(self,i,val):
		self.board[i]=val
	
	def __str__(self):
		s = ''
		for row in range (Board.MAX):
			for col in range(Board.MAX):
				s += str(self.board[row][col])
				if col < Board.MAX-1:
					s += "|"
			if row < Board.MAX-1:
				s += "\n"
		return s
	