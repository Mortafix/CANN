import numpy as np

### Example Table ###
# x1 x2 x3 y
# 0	 0	1  0
# 0	 1	1  1
# 1	 0	1  1
# 1	 1	1  0

 
# Sigmoid function
def sigmoid(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

# Analyze if goal is reached
def goal(w,p):
	res = True
	for i in range(0,len(w)):
		if goal_perc(w[i],y[i],p):
			res = False
	return res

# Single weight test
def goal_perc(w,o,p):
	if o == 1:
		return w < p
	else:
		return w > (1-p)
 
# Times of loop and Percentage goal
loop_n,perc = 100000,0.995
 
# Input
x = np.array([[1,0,1],[0,1,1],[0,0,1],[1,1,1]])
 
# Output           
y = np.array([[0,1,1,0]]).transpose()

# Initialize weights
wei0 = np.random.random((3,4))
wei1 = np.random.random((4,1))
 
i,l0,l1,l2 = 0,[0,0,0,0],[0,0,0,0],[0,0,0,0] 
while i < loop_n and not goal(l2,perc):

	# Forward propagation
	l0 = x
	l1 = sigmoid(np.dot(l0,wei0))
	l2 = sigmoid(np.dot(l1,wei1))

	# Error from output (how much we missed)
	l2_error = y - l2
 
	# Multiply error by derivate of the sigmoid at the values in l2 (how much we have to change the weights)
	l2_delta = l2_error * sigmoid(l2,True)

	# Contribute of l1 to the l2 error (according to the weights)
	l1_error = np.dot(l2_delta,wei1.transpose())
	
	# Multiply error by derivate of the sigmoid at the values in l1 (how much we have to change the weights)
	l1_delta = l1_error * sigmoid(l1,True)
	 
	# Update weights
	wei0 += np.dot(l0.transpose(),l1_delta)
	wei1 += np.dot(l1.transpose(),l2_delta)

	i += 1

print("Output:")
print(l2)
if(goal(l2,perc)):
	print(str(i)+" times for a "+str(perc*100)+"% win rate")
else:
	print("Goal for a "+str(perc*100)+"% win rate not reached in "+str(loop_n)+" times")
