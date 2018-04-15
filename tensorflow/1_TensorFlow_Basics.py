import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# What we expect
X = np.random.rand(100).astype(np.float32)
a = 50
b = 40
Y = a * X + b
plt.plot(X,Y)

# Setting the training variables
Y = np.vectorize(lambda y: y + np.random.normal(loc=0.0, scale=0.05))(Y)
a_var = tf.Variable(1.0)
b_var = tf.Variable(1.0)
y_var = a_var * X + b_var

# minimizing the mean squared error
loss = tf.reduce_mean(tf.square(y_var - Y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Learning
TRAINING_STEPS = 300
results = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(TRAINING_STEPS):
        results.append(sess.run([train, a_var, b_var])[1:])

# Final Prediction
final_pred = results[-1]
a_pred = final_pred[0]
b_pred = final_pred[1]
y_pred = a_pred * X + b_pred
print("a:", a_pred, "b:", b_pred)

# Expectation vs Prediction
plt.plot(X, Y)
plt.plot(X, y_pred)
