import numpy as np

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

def bot_simulate():
	bot1_move_int = np.random.randint(3)
	bot2_move_int = np.random.randint(3)
	bot1_move = 'r'
	bot2_move = 'r'
	if bot1_move_int == 0:
		bot1_move = 's'
	elif bot1_move_int == 1:
		bot1_move = 'p'
	if bot2_move_int == 0:
		bot2_move = 's'
	elif bot2_move_int == 1:
		bot2_move = 'p'
	return who_wins(bot1_move,bot2_move)

first_command = raw_input('n - Player vs Bot\nv - Player vs Player\nb - Bot vs Bot\nq - quit\nCommand: ')
while first_command != 'q':

	if first_command == 'v':
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

	elif first_command == 'n':
		print ""
		print "r - rock\np - paper\ns - scissors\n"
		p1_cmd = raw_input("Player move: ")
		while p1_cmd != 'r' and p1_cmd != 'p' and p1_cmd != 's':
			p1_cmd = raw_input('Command not allowed. Retry: ')
		bot_move_int = np.random.randint(3)
		bot_move = 'r'
		if bot_move_int == 0:
			bot_move = 's'
		elif bot_move_int == 1:
			bot_move = 'p'
		print "Bot Move: " + bot_move
		print ""
		res = who_wins(p1_cmd,bot_move)
		if res == 0:
			print "Draw!"
		elif res == 1:
			print "Player wins!"
		elif res == 2:
			print "Bot wins!"

	elif first_command == 'b':
		print ""
		times = int(input("How many games? "))
		i,games = 0,{}
		while i < times:
			res = bot_simulate()
			if res == 0:
				str_res = "Draw!"
			elif res == 1:
				str_res = "Bot 1 wins!"
			elif res == 2:
				str_res = "Bot 2 wins!"
			if str_res in games:
				games[str_res] += 1
			else:
				games[str_res] = 1
			i += 1
		print ""
		print np.array(sorted(games.items(),key=lambda n: n[1], reverse=True)).transpose()

	print "\n######################################"
	first_command = raw_input('n - Player vs Bot\nv - Player vs Player\nb - Bot vs Bot\nq - quit\nCommand: ')
