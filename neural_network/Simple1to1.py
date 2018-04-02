import numpy as np

### Example Table ###
# x1 x2 x3 y
# 0	 0	1  0
# 0	 1	1  0
# 1	 0	1  1
# 1	 1	1  1

 
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
loop_n,perc = 10000,0.98
 
# Input
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
 
# Output           
y = np.array([[0,0,1,1]]).transpose()
 
# Initialize weights
#wei0 = np.random.random((3,1)) # random weights
wei0 = np.array([[0.5,0.5,0.5]]).transpose()

i,l1 = 0,[0,0,0,0] 
while i < loop_n and not goal(l1,perc):

	# Forward propagation
	l0 = x
	l1 = sigmoid(np.dot(l0,wei0))

	# error from output (how much we missed)
	l1_error = y - l1

	# multiply error by derivate of the sigmoid at the values in l1 (how much we have to change the weights)
	l1_delta = l1_error * sigmoid(l1,True)

	# Update weights
	wei0 += np.dot(l0.transpose(),l1_delta)

	i += 1

print("Output:")
print(l1)
if(goal(l1,perc)):
	print(str(i)+" times for a "+str(perc*100)+"% win rate")
else:
	print("Goal for a "+str(perc*100)+"% win rate not reached in "+str(loop_n)+" times")
