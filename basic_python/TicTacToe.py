import numpy as np

def print_example_board():
	res = ""
	res += print_line()
	res += "\n"
	res += "| 1 | 2 | 3 |"
	res += "\n"
	res += print_line()
	res += "\n"
	res += "| 4 | 5 | 6 |"
	res += "\n"
	res += print_line()
	res += "\n"
	res += "| 7 | 8 | 9 |"
	res += "\n"
	res += print_line()
	print(res)

def print_board(board):
	res = ""
	for i in range(0,3):
		res += print_line()
		res += "\n"
		res += print_column(board[i])
		res += "\n"
	res += print_line()
	print(res)

def print_line():
	return "  -   -   -"

def print_column(seq):
	sym1,sym2,sym3 = " "," "," "
	if seq[0] == 1:
		sym1 = "X"
	elif seq[0] == 2:
		sym1 = "O"
	if seq[1] == 1:
		sym2 = "X"
	elif seq[1] == 2:
		sym2 = "O"
	if seq[2] == 1:
		sym3 = "X"
	elif seq[2] == 2:
		sym3 = "O"
	return "| "+sym1+" | "+sym2+" | "+sym3+" |"


def check_win(board):
	res = 0
	res = check_diag(board)
	if res != 0:
		return res
	res = check_line(board)
	if res != 0:
		return res
	return res


def check_diag(board):
	if (board[0][0] + board[1][1] + board[2][2] == 3) or (board[0][2] + board[1][1] + board[2][0] == 3):
		return 1
	elif (board[0][0] + board[1][1] + board[2][2] == 6) or (board[0][2] + board[1][1] + board[2][0] == 3):
		return 2
	else:
		return 0

def check_line(board):
	res = 0
	for i in range(0,3):
		if (board[i][0] + board[i][1] + board[i][2] == 3) or (board[0][i] + board[1][i] + board[2][i] == 3):
			res = 1
		elif (board[i][0] + board[i][1] + board[i][2] == 6) or (board[0][i] + board[1][i] + board[2][i] == 6):
			res = 2
	return res

def coord_move(move):
	if move == "1":
		return (0,0)
	elif move == "2":
		return (0,1)
	elif move == "3":
		return (0,2)
	elif move == "4":
		return (1,0)
	elif move == "5":
		return (1,1)
	elif move == "6":
		return (1,2)
	elif move == "7":
		return (2,0)
	elif move == "8":
		return (2,1)
	elif move == "9":
		return (2,2)
	else:
		return None

def ask_move(p):
	p_move = input("Player "+str(p)+" moves: ")
	while coord_move(p_move) == None:
		p_move = input("Wrong move: ")
	return coord_move(p_move)

def bot_move(b):
	b_move = np.random.randint(1,10)
	return coord_move(str(b_move))


print("MOVE SET")
print_example_board()
print("")
first_command = input('n - Player vs Player\nb - Bot vs Bot\nq - quit\nCommand: ')
while first_command != 'q':
	n,i = 100,0
	board = [[n,n,n],[n,n,n],[n,n,n]]
	if first_command == 'n':
		while check_win(board) == 0:
			if i < 9:
				turn = i % 2
				valid = 0
				while valid == 0:
					move = ask_move(turn + 1)
					if board[move[0]][move[1]] != n:
						print("Cell not empty!")
					else:
						valid = 1
						board[move[0]][move[1]] = turn + 1
				if check_win(board) != 0:
					print("\nPLAYER "+str(turn+1)+" WINS!")
					print_board(board)
				else:
					print_board(board)
					i += 1
			else:
				print("\nBoard full. DRAW!")
				break

	elif first_command == 'b':
		while check_win(board) == 0:
			if i < 9:
				turn = i % 2
				valid = 0
				while valid == 0:
					move = bot_move(turn + 1)
					if board[move[0]][move[1]] == n:
						valid = 1
						board[move[0]][move[1]] = turn + 1
				if check_win(board) != 0:
					print("\nBOT "+str(turn+1)+" WINS!")
					print_board(board)
				else:
					i += 1
			else:
				print("\nBoard full. DRAW!")
				print_board(board)
				break

	print("\n######################")
	first_command = input('n - Player vs Player\nb - Bot vs Bot\nq - quit\nCommand: ')


