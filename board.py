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
				if self.board[row][col]==Board.BLANK:
					return False
		return True
	
	def is_empty_spot(self,row,col):
		return self.board[row][col] == Board.BLANK
	
	def find_empty_spots(self):
		lst=[]
		for row in range(Board.MAX):
			for col in range(Board.MAX):
				if self.is_empty_spot(row,col):
					lst.append([row,col])
		return lst
	
	#TODO: return first location found, where its corresponding row/col/diagonal is almost complete
	def find_near_full(self,sym):
		loc = None
		for dgn in range(Board.DGN):
			loc = self.find_near_full_diagonal(sym,dgn)
			if loc != None:
				return loc
			
		for row in range(Board.MAX):
			loc = self.find_near_full_row(sym,row)
			if loc != None:
				return loc
			
		for col in range(Board.MAX):
			loc = self.find_near_full_col(sym,col)
			if loc != None:
				return loc

		return loc
	
	def find_near_full_row(self,sym,row):
		syms=[]
		loc=None
		for col in range(Board.MAX):
			if sym == self.board[row][col]:
				syms.append(sym)
			elif Board.BLANK == self.board[row][col]:
				loc = [row,col]
		if len(syms) != Board.MAX-1:
			loc=None
		return loc
		
	def find_near_full_col(self,sym,col):
		syms=[]
		loc=None
		for row in range(Board.MAX):
			if sym == self.board[row][col]:
				syms.append(sym)
			elif Board.BLANK == self.board[row][col]:
				loc = [row,col]
		if len(syms) != Board.MAX-1:
			loc=None
		return loc
		
	def find_near_full_diagonal(self,sym,dgn):
		syms=[]
		loc=None
		
		if dgn == 0:
			for i in range(Board.MAX):
				if sym == self.board[i][i]:
					syms.append(sym)
				elif Board.BLANK == self.board[i][i]:
					loc = [i,i]
			if len(syms) != Board.MAX-1:
				loc = None
					
		elif dgn == 1:
			col = Board.MAX-1
			for row in range(Board.MAX):
				if sym == self.board[row][col]:
					syms.append(sym)
				elif Board.BLANK == self.board[row][col]:
					loc = [row,col]
				col-=1
			if len(syms) != Board.MAX-1:
				loc = None
		return loc
	
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
	