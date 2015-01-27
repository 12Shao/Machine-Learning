# everything in this script is stolen from http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html
# the only difference is that I wanted to make a class instead of seperate functions

import numpy as np

class LinReg(object):
    '''Classic linear regression
    First try at simple linear regression class in python
    takes five arguments: train_X, train_y, alpha, theta, iterations for SGD
    '''
    def __init__(self, X, y, alpha, iterations):
        self.X = X
        self.y = y
        self.alpha = alpha
        self.iterations = iterations
        self.theta = np.zeros(shape = (2,1))
    
    def compute_cost(self):
        m = self.y.size
		
        predictions = self.X.dot(self.theta).flatten()

        sqErrors = (predictions - y) ** 2
		
        return (1.0 / (2 * m)) * sqErrors.sum()
    
    def gradient_descent(self):
        X = self.X
        y = self.y
        m = y.size
        theta = self.theta
        J_history = np.zeros(shape = (self.iterations, 1))
        
        for i in range(self.iterations):
            predictions = X.dot(self.theta).flatten()
			
            errors_x1 = (predictions - y) * X[:,0]
            errors_x2 = (predictions - y) * X[:,1]
			
            theta[0][0] = theta[0][0] - self.alpha * (1.0 / m) * errors_x1.sum()
            theta[1][0] = theta[1][0] - self.alpha * (1.0 / m) * errors_x2.sum()
			
            J_history[i, 0] = self.compute_cost()
            if i % 100 == 0:
                print 'theta:', theta
        
        self.theta = theta
        return theta, J_history
        
    def predict(self, X):
        prediction = X.dot(theta).flatten()
        return prediction


# initialize linear regression parameters
iterations = 1500
alpha = 0.001

# load the example data stolen from 'http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html'
data = np.loadtxt('ex1data1.txt', delimiter = ',')
X = data[:,0]
y = data[:,1]

# add a column of ones to X (intercept data)
m = y.size
it = np.ones(shape = (m,2))
it[:,1] = X
#print it

# plot the data with seaborn (add this later)

# fit the linear reg
linearReg = LinReg(X = it, y = y, alpha = alpha, iterations = iterations)
theta, J_history = linearReg.gradient_descent()

# make a predictions with X = 3.5
print linearReg.predict(np.array([1, 3.5]))