"""utils"""
import board
from board import *
	
def read_input(fname):
# read in input for checker tests
	boards = []
	with open(fname,'r') as file:
		row=0
		col=0
		boards_idx=0
		boards.append(Board())
		for line in file:
			line = line.strip()
			#print line
			if len(line) == 0:
				continue
			for sym in line:
				#print sym
				boards[boards_idx][row][col]=sym.upper()
				if col < Board.MAX-1:
					col+=1
				else:
					if row < Board.MAX-1:
						row+=1
						col=0
					else:
						#print "LIM Reached!"
						boards.append(Board())
						boards_idx+=1
						row=0
						col=0
	return boards[:len(boards)-1]

