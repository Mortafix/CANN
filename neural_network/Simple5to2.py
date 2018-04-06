import numpy as np

### Example Table ###
# x1 x2 x3 x4 x5 y1 y2
# 0	 0	1  1  0  0  0
# 0	 1	0  0  0  0  1
# 0	 0	1  1  1  0  0
# 0	 1	1  0  0  0  1
# 1	 0	0  1  0  0  0
# 1	 1	0  0  0  0  0
# 1	 0	1  0  0  0  0
# 1	 1	0  1  0  1  0

 
# Sigmoid function
def sigmoid(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

# Analyze if goal is reached
def goal(w,p):
	res = True
	for i in range(0,len(w[0])):
		if goal_perc(w[0][i],y[i][0],p):
			res = False
		if goal_perc(w[1][i],y[i][1],p):
			res = False
	return res

# Single weight test
def goal_perc(w,o,p):
	if o == 1:
		return w < p
	else:
		return w > (1-p)
 
# Times of loop and Percentage goal
loop_n,perc = 100000,0.99
 
# Input
x = np.array([[0,0,1,1,0],[0,1,1,0,0],[0,0,1,1,1],[0,1,1,0,0],[1,0,0,1,0],[1,1,0,0,0],[1,0,1,0,0],[1,1,0,1,0]])
 
# Output           
y = np.array([[0,0,0,0,0,0,0,1],[0,1,0,1,0,0,0,0]]).transpose()

# Initialize weights with mean 0
wei0 = 2*np.random.random((5,8))-1
wei1 = 2*np.random.random((8,8))-1
wei2 = 2*np.random.random((8,8))-1
wei3 = 2*np.random.random((8,8))-1
wei4 = 2*np.random.random((8,2))-1
 
i,l5 = 0,[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] 
while i < loop_n and not goal(l5,perc):

	# Forward propagation
	l0 = x
	l1 = sigmoid(np.dot(l0,wei0))
	l2 = sigmoid(np.dot(l1,wei1))
	l3 = sigmoid(np.dot(l2,wei2))
	l4 = sigmoid(np.dot(l3,wei3))
	l5 = sigmoid(np.dot(l4,wei4))

	l5_error = y - l5
	l5_delta = l5_error * sigmoid(l5,True)

	l4_error = np.dot(l5_delta,wei4.transpose())
	l4_delta = l4_error * sigmoid(l4,True)

	l3_error = np.dot(l4_delta,wei3.transpose())
	l3_delta = l3_error * sigmoid(l3,True)

	l2_error = np.dot(l3_delta,wei2.transpose())
	l2_delta = l2_error * sigmoid(l2,True)

	l1_error = np.dot(l2_delta,wei1.transpose())
	l1_delta = l1_error * sigmoid(l1,True)
	 
	wei0 += np.dot(l0.transpose(),l1_delta)
	wei1 += np.dot(l1.transpose(),l2_delta)
	wei2 += np.dot(l2.transpose(),l3_delta)
	wei3 += np.dot(l3.transpose(),l4_delta)
	wei4 += np.dot(l4.transpose(),l5_delta)

	i += 1

res = []
bool_res = goal(l5,perc)
print("Output:")
print(l5)
if(bool_res):
	print(str(i)+" times for a "+str(perc*100)+"% win rate")
else:
	print("Goal for a "+str(perc*100)+"% win rate not reached in "+str(loop_n)+" times")
