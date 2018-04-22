import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
from math import *

# Settings
sns.set(style='whitegrid', palette='muted', font_scale=1.5)
rcParams['figure.figsize'] = 12, 6
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Sigmoid functions
def sigmoid_single(n):
	return 1/(1+exp(-n))
def sigmoid_prime_single(n):
	return exp(-n)/(1+exp(-n))**2
sigmoid = np.vectorize(sigmoid_single)
sigmoid_prime = np.vectorize(sigmoid_prime_single)

# Sigmoid plot
x = np.linspace(-10., 10., num=100)
sig = sigmoid(x)
sig_prime = sigmoid_prime(x)
plt.plot(x, sig, label="sigmoid")
plt.plot(x, sig_prime, label="sigmoid prime")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(prop={'size' : 16})
plt.show()

# NN parameters
epochs = 50000
input_size, hidden_size, output_size = 2, 3, 1
LR = 0.1
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([ [0],   [1],   [1],   [0]])
w_hidden = np.random.uniform(size=(input_size, hidden_size))
w_output = np.random.uniform(size=(hidden_size, output_size))

# Training loop
for epoch in range(epochs):
 
    # Forward
    act_hidden = sigmoid(np.dot(X, w_hidden))
    output = np.dot(act_hidden, w_output)
    
    # Error
    error = y - output
    
    # Backward
    dZ = error * LR
    w_output += act_hidden.T.dot(dZ)
    dH = dZ.dot(w_output.T) * sigmoid_prime(act_hidden)
    w_hidden += X.T.dot(dH)

print(output)