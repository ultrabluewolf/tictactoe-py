"""Board Validation methods"""

import board
from board import *

"""check board for a winner"""
def is_winner(board):
	result = Board.BLANK
	
	for dgn in range(Board.DGN):
		result = check_diagonal_win(board,dgn)
		if not is_blank(result):
			return result
	
	for row in range(Board.MAX):
		result = check_row_win(board,row)
		if not is_blank(result):
			return result
	
	for col in range(Board.MAX):
		result = check_col_win(board,col)
		#if not is_blank(result):
		#	return result
	
	return result

def check_row_win(board,row):
	crosses=[]
	circs=[]
	for col in range(Board.MAX):
		if is_cross(board[row][col]):
			crosses.append(Board.CROSS)
			if len(crosses) == Board.MAX:
				return Board.CROSS
		elif is_circ(board[row][col]):
			circs.append(Board.CIRC)
			if len(circs) == Board.MAX:
				return Board.CIRC
	return Board.BLANK

def check_col_win(board,col):
	crosses=[]
	circs=[]
	for row in range(Board.MAX):
		if is_cross(board[row][col]):
			crosses.append(Board.CROSS)
			if len(crosses) == Board.MAX:
				return Board.CROSS
		elif is_circ(board[row][col]):
			circs.append(Board.CIRC)
			if len(circs) == Board.MAX:
				return Board.CIRC
	return Board.BLANK

def check_diagonal_win(board,dgn):
	crosses=[]
	circs=[]
	if dgn == 0:
		for i in range(Board.MAX):
			if is_cross(board[i][i]):
					crosses.append(Board.CROSS)
					if len(crosses) == Board.MAX:
						return Board.CROSS
			elif is_circ(board[i][i]):
				circs.append(Board.CIRC)
				if len(circs) == Board.MAX:
					return Board.CIRC
	elif dgn == 1:
		col = Board.MAX-1
		for row in range(Board.MAX):
			if is_cross(board[row][col]):
				crosses.append(Board.CROSS)
				if len(crosses) == Board.MAX:
					return Board.CROSS
			elif is_circ(board[row][col]):
				circs.append(Board.CIRC)
				if len(circs) == Board.MAX:
					return Board.CIRC
			col-=1
	return Board.BLANK

def is_blank(sym):
	return sym == Board.BLANK
def is_cross(sym):
	return sym == Board.CROSS
def is_circ(sym):
	return sym == Board.CIRC

def get_opposite(sym):
	if sym == Board.CROSS:
		return Board.CIRC
	elif sym == Board.CIRC:
		return Board.CROSS
	else:
		return Board.BLANK
