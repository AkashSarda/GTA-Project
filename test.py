def get_B(board):
	B = []
	for item in range(1, 9):
		B.append(board.index(item))
	B.append(board.index(0))
	return B

def NMaxSwap(board):
	final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
	P = board[:]
	B = get_B(P)
	print P, B
	while(not final_state == P):
		P[B[8]], P[B[B[8]]] = P[B[B[8]]], P[B[8]]
		B = get_B(P)
		print P, B
	print "done."

board = [2, 0, 6, 1, 3, 4, 7, 5, 8]
NMaxSwap(board)