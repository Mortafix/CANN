import numpy as np

# u -> 0 -> Blank DOWN
# d -> 1 -> Blank UP
# l -> 2 -> Blank RIGHT
# r -> 3 -> Blank LEFT

def print_board(board,dim):
	res = ""
	for i in xrange(0,dim):
		res += print_line(dim)
		res += "\n"
		res += print_column(board[i],dim)
		res += "\n"
	res += print_line(dim)
	print res

def print_line(dim):
	n_len = len(str(dim*dim))
	s = "  "
	for i in xrange(0,dim):
		for j in xrange(0,n_len):
			s += "-"
		s += "   "
	return s

def print_number(n,dim):
	n_s,s = str(n),""
	n_len = len(str(dim*dim))
	if n != 0:
		for i in xrange(0,n_len-len(n_s)):
			s += " "
		s += n_s
	else:
		for i in xrange(0,n_len):
			s += " "
	return s

def print_column(seq,dim):
	line = "| "
	for i in xrange(0,dim):
		line += print_number(seq[i],dim)
		line += " | "
	return line

def create_random_board(dim):
	board = list(range(0,(dim*dim)))
	np.random.shuffle(board)
	return [board[i:i+dim] for i in xrange(0,len(board),dim)]
		
def find_blank(board,dim):
	for i in xrange(0,dim):
		for j in xrange(0,dim):
			if board[i][j] == 0:
				return (i,j)

def is_valid_move(board,move,dim):
	coord = find_blank(board,dim)
	if move == 0:
		if coord[0] == (dim-1):
			return False
		else:
			return True
	elif move == 1:
		if coord[0] == 0:
			return False
		else:
			return True
	elif move == 2:
		if coord[1] == (dim-1):
			return False
		else:
			return True
	elif move == 3:
		if coord[1] == 0:
			return False
		else:
			return True

def make_move(board,move,dim):
	coord = find_blank(board,dim)
	if move == 0:
		switch = (coord[0]+1,coord[1])
	elif move == 1:
		switch = (coord[0]-1,coord[1])
	elif move == 2:
		switch = (coord[0],coord[1]+1)
	elif move == 3:
		switch = (coord[0],coord[1]-1)
	temp = board[switch[0]][switch[1]]
 	board[switch[0]][switch[1]] = board[coord[0]][coord[1]]
 	board[coord[0]][coord[1]] = temp

def is_board_complete(board,dim):
	index = 1
	for i in xrange(0,dim):
		for j in xrange(0,dim):
			if index != (dim*dim):
				if board[i][j] != index:
					return False
				else:
					index += 1
	return True

def inversions_number(board,dim):
	board_stretch,total = [],0
	for i in xrange(0,dim):
		board_stretch += board[i]
	for j in xrange(0,len(board_stretch)):
		for k in xrange(j+1,len(board_stretch)):
			if board_stretch[j] != 0 and board_stretch[k] != 0:
				if board_stretch[j] > board_stretch[k]:
					total += 1
	return total


def is_resolvable(board,dim):
	inv = inversions_number(board,dim)
	if dim%2 == 1:
		if inv%2 == 0:
			return True
		else:
			return False
	else:
		bottom = dim-find_blank(board,dim)[0]
		if bottom%2 == 0:
			if inv%2 == 1:
				return True
			else:
				return False
		else:
			if inv%2 == 0:
				return True
			else:
				return False
		

first_command = raw_input('p - Player\nb - Random Bot\nh - help\nq - quit\nCommand: ')
while first_command != 'q':

	if first_command == 'p':
		dim = int(input("How big? (NxN): "))
		board = create_random_board(dim)
		print_board(board,dim)
		if is_resolvable(board,dim):
			total_move = 0
			while not is_board_complete(board,dim):
				move = raw_input("Move: ")
				if move == "u":
					move_int = 0
				elif move == "d":
					move_int = 1
				elif move == "l":
					move_int = 2
				elif move == "r":
					move_int = 3
				elif move == "f":
					print "\nSo bad! Board not complete."
					break
				if is_valid_move(board,move_int,dim):
					total_move += 1
					make_move(board,move_int,dim)
					print_board(board,dim)
			if is_board_complete(board,dim):
				print "\nGREAT! Board Complete.\nTotal move: "+str(total_move)
		else:
			print "Not Resolvable! Try shuffle again."

	elif first_command == 'b':
		dim = int(input("How big? (NxN): "))
		board = create_random_board(dim)
		print_board(board,dim)
		if is_resolvable(board,dim):
			total_move = 0
			while not is_board_complete(board,dim):
				rnd_move = np.random.randint(0,4)
				if is_valid_move(board,rnd_move,dim):
					total_move += 1
					make_move(board,rnd_move,dim)
			print "\nGREAT! Board Complete.\nTotal move: "+str(total_move)
			print_board(board,dim)
		else:
			print "Not Resolvable! Try shuffle again."

	elif first_command == "h":
		print "\n#  MOVE SET  #\n#  u - Up\n#  d - Down\n#  l - Left\n#  r - Right\n#  f - Forfeit"

	print "\n#################"
	first_command = raw_input('p - Player\nb - Random Bot\nh - Help\nq - quit\nCommand: ')



