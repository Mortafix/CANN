# 0 : Draw
# 1 : P1 wins
# 2 : P2 wins
def who_wins(p1_move,p2_move):
	if p1_move == p2_move:
		return 0
	else:
		if (p1_move == "r" and p2_move == "s") or (p1_move == 'p' and p2_move == 'r') or (p1_move == 's' and p2_move == 'p'):
			return 1
		else:
			return 2 

first_command = raw_input('n - new game\nq - quit\nCommand: ')
while first_command != 'q':
	if first_command == 'n':
		print ""
		print "r - rock\np - paper\ns - scissors\n"
		p1_cmd = raw_input("Player 1 move: ")
		while p1_cmd != 'r' and p1_cmd != 'p' and p1_cmd != 's':
			p1_cmd = raw_input('Command not allowed. Retry: ')
		p2_cmd = raw_input("Player 2 move: ")
		while p2_cmd != 'r' and p2_cmd != 'p' and p2_cmd != 's':
			p2_cmd = raw_input('Command not allowed. Retry: ')
		print ""
		res = who_wins(p1_cmd,p2_cmd)
		if res == 0:
			print "Draw!"
		elif res == 1:
			print "Player 1 wins!"
		elif res == 2:
			print "Player 2 wins!"
	first_command = raw_input('\nn - new game\nq - quit\nCommand: ')