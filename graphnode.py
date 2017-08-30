class State:
	def __init__(self, board_state, dimension):
		self.state = board_state # board object
		self.dimension = dimension
	
	def heuristic(self):
		heuristic = 0
		for i in self.dimension:
			for j in self.dimension:
				pass #write the manhattan distance formula
		return heuristic

	def giveNeighbours(self):
		pass

class Board:
	def __init__(self, dimension = 3):
		self.dimension = dimension
		self.board = [0] * dimension * dimension
		self.emp = False

	def populate(self):
		for i in range(self.dimension):
			for j in range(self.dimension):
				x = int(input("Enter at %d %d location" % (i, j)))
				if x == -1 and not self.emp:
					self.emp_cell = (i, j)
					self.emp = True
					continue
				elif x == -1 and self.emp:
					print "Only one empty cell!"
					break
				self.board[i*self.dimension + j] = x

	def display(self):
		for i in range(self.dimension * self.dimension):
			print self.board[i]

def Solver:
	def __init__(self, board_obj):
		self.ini_state = State(board_obj, board_obj.dimension)
		self.dimension = board_obj.dimension

	def solver:
		s = 

b = Board()
b.populate()
