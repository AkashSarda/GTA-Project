class State:
	def __init__(self, board_state, dimension): # all fine
		self.board_state = board_state # board object
		self.state = board_state.board # board list
		self.dimension = dimension
		self.emp_cell = board_state.emp_cell
		self.heuristic = self.heuristic()

	def heuristic(self):
		heuristic = 0
		for i in range(self.dimension):
			for j in range(self.dimension):
				if self.state[i*self.dimension + j] == 0:
					heuristic += abs(i - self.dimension + 1) + abs(j - self.dimension + 1)
					continue
				x = (self.state[i*self.dimension + j] - 1) / self.dimension
				y = (self.state[i*self.dimension + j] - 1) - x * self.dimension
				heuristic += (abs(x - i) + abs(y - j))
#				print "x : %d y : %d i : %d j : %d " % (x, y, i, j)
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

	def isempty(self):
		if self.qu == []:
			return False
		return True

class Solver:
	def __init__(self, board_obj):
		self.ini_state = State(board_obj, board_obj.dimension)
		self.dimension = board_obj.dimension

	def solver(self):
		s = self.ini_state
		q = PriorityQueue()
		ideal_state = [i + 1 for i in range(0, self.dimension * self.dimension)]
		ideal_state[self.dimension * self.dimension - 1] = 0
		visited = []
		q.enqueue((0, s)) # weight, current state
		moves = 0
		found = False
		# print q.isempty()
		while q.isempty():
			mst = q.dequeue()
			if mst[1].state == ideal_state:
				found = True
				print "Found after %d moves" % (moves)
				visited.append(mst[1].state)
				break
			if mst[1].state in visited:
				continue
			visited.append(mst[1].state)
			# print "visited ::::: " + str(visited)
			moves += 1 # recording the parent
			for nei in mst[1].giveNeighbours():
				if nei.state not in visited:
					q.enqueue((moves + nei.heuristic,nei))
					# print "enqueueing " + str(nei.state)
		return visited

def print_as_board(b):
	st = ''
	for i in range(9):
		if (i + 1) % 3 == 0:
			st += '| '+ str(b[i]) + ' |\n'	
		else:
			st += '| '+ str(b[i]) + ' |'	
	print st


b = Board()
# b.duplicate([1,5,4,8,6,2,7,3,0], b.dimension)
#b.duplicate([4,1,3,7,2,5,0,8,6], b.dimension)
b.duplicate([4,1,3,2,0,5,7,8,6], b.dimension)
#b.duplicate([1,3,6,5,0,2,4,7,8], b.dimension)
sol = Solver(b)
for i in sol.solver():
	print_as_board(i)
