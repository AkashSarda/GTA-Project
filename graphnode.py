class State:
	def __init__(self, board_state, dimension): # all fine
		self.board_state = board_state # board object
		self.state = board_state.board # board list
		self.dimension = dimension
		self.emp_cell = board_state.emp_cell	
#		self.heuristic = self.heuristic()
	
	def heuristic(self):
		heuristic = 0
		for i in self.dimension:
			for j in self.dimension:
				pass #write the manhattan distance formula
		return heuristic

	def swap(self, a,b): # because of the fuck-up ive done when calling this function.
		return (a,b)

	def giveNeighbours(self): 
		neighbours = []
		x = self.emp_cell[0]
		y = self.emp_cell[1]
		
		if not x + 1 >= self.dimension:
			buff = []
			buff.extend(self.state)
			buff[x*self.dimension + y], buff[(x+1)*self.dimension + y] = self.swap(buff[(x+1)*self.dimension + y],buff[x*self.dimension + y])
			bd = Board(self.dimension)
			bd.duplicate(buff, self.dimension)
			st = State(bd, self.dimension)
			#print buff
			neighbours.append(st)

		if not y + 1 >= self.dimension:
			buff = []
			buff.extend(self.state)
			buff[x*self.dimension + y], buff[x*self.dimension + y + 1] = self.swap(buff[(x)*self.dimension + y + 1],buff[x*self.dimension + y])
			
			bd = Board(self.dimension)
			bd.duplicate(buff, self.dimension)
			st = State(bd, self.dimension)
			#print buff
			neighbours.append(st)

		
		if not x - 1 < 0:
			buff = []
			buff.extend(self.state)
			buff[x*self.dimension + y], buff[(x-1)*self.dimension + y] = self.swap(buff[(x-1)*self.dimension + y],buff[x*self.dimension + y])
			bd = Board(self.dimension)
			bd.duplicate(buff, self.dimension)
			st = State(bd, self.dimension)
			#print buff
			neighbours.append(st)

		if not y - 1 < 0:
			buff = []
			buff.extend(self.state)
			buff[x*self.dimension + y], buff[x*self.dimension + y - 1] = self.swap(buff[(x)*self.dimension + y-1],buff[x*self.dimension + y])
			bd = Board(self.dimension)
			bd.duplicate(buff, self.dimension)
			st = State(bd, self.dimension)
			#print buff, self.state
			neighbours.append(st)

		return neighbours

	def display(self): # works fine
		print self.state, self.emp_cell

class Board:
	def __init__(self, dimension = 3):
		self.dimension = dimension
		self.board = [0] * dimension * dimension
		self.emp = False
	
	def duplicate(self, buff, dimension):
		self.board = buff
		self.dimension = dimension
		a = False
		for i in range(self.dimension):
			for j in range(self.dimension):
				if buff[i * self.dimension + j] == 0:
					self.emp_cell = (i, j)
					a = True
					break
			if a:
				break

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

class PriorityQueue:
	def __init__(self):
		self.qu = []

	def enqueue(self, obj):
		self.qu.append(obj)

	def dequeue(self):
		if self.qu == []:
			return False

		self.qu.sort()
		a = self.qu[0]
		self.qu = self.qu[1:]
		return a

class Solver:
	def __init__(self, board_obj):
		self.ini_state = State(board_obj, board_obj.dimension)
		self.dimension = board_obj.dimension

	def solver(self):
		s = self.ini_state
		q = PriorityQueue()
		ideal_state = [i for i in range(1, self.dimension * self.dimension - 1)]
		visited = {}
		q.enqueue((0, st)) # weight, current state
		weights = {} # should record parents here.
		weights[s] = (0, None) # weight, parent
		weight = 0
		found = False

		while True:
			mst = q.dequeue()
			#mst[0] is the weight, mst[1] is the tuple. mst[1][0] is current, mst[1][1] is the parent.
			if mst[1].state == ideal_state:
				found = True
				break

			if mst[1] in visited.keys():
				continue

			visited[mst[1]] = weights[mst[1]][1] # recording the parent
			for nei in mst[1].getNeighbours():
				if nei not in weights.keys():
					weights[nei] = (mst[1].heuristic + nei.heuristic, mst[1])
					q.enqueue((weights[nei], nei))
					continue
				else:
					if mst[1].heuristic + nei.heuristic > weights[nei][0]:
						weights[nei] = (mst[1].heuristic + nei.heuristic, mst[1])


b = Board()
b.duplicate([1,2,4,5,0,3,7,8,6], b.dimension)
st = State(b, b.dimension)
for nei in st.giveNeighbours():
	print nei.state
