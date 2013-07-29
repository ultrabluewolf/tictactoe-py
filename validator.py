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
		if not is_blank(result):
			return result

def check_row_win(board,row):
	pass

def check_col_win(board,col):
	pass

def check_diagonal_win(board,dgn):
	pass

def is_blank(sym):
	return sym == Board.BLANK

