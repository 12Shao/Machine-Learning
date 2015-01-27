# everything in this script is stolen from http://aimotion.blogspot.com/2011/10/machine-learning-with-python-linear.html
# the only difference is that I wanted to make a class instead of seperate functions

import numpy as np

class LinReg(object):
    '''Classic linear regression
    First try at simple linear regression class in python
    takes two arguments: alpha (learning rate), number of iterations for SGD
    '''
    def __init__(self, alpha, iterations, tolerance):
        self.alpha = alpha
        self.iterations = iterations
        self.tolerance = tolerance
        self.theta = np.zeros(shape = (2,1))
    
    def compute_cost(self, X, y, theta):
		""" Calculate mean squared error by subtracting true from predicted
		and dividing by 2
		:return: mean squared error
		"""
        m = y.size
		
        predictions = X.dot(theta).flatten()

        sqErrors = (predictions - y) ** 2
		
        return (1.0 / (2 * m)) * sqErrors.sum()
    
    def gradient_descent(self, X, y):
		""" Search algorithm - loops over theta and updates to
		 take steps in direction of steepest decrease of J.
		:return: value of theta that minimizes J(theta) and J_history
		"""
        m = y.size
        theta = self.theta
        J_history = np.zeros(shape = (self.iterations, 1))
        
        i = 0
        tol = 1
        #for i in range(self.iterations):
        while tol > self.tolerance:
            predictions = X.dot(theta).flatten()
			
            errors_x1 = (predictions - y) * X[:,0]
            errors_x2 = (predictions - y) * X[:,1]
			
            theta[0][0] = theta[0][0] - self.alpha * (1.0 / m) * errors_x1.sum()
            theta[1][0] = theta[1][0] - self.alpha * (1.0 / m) * errors_x2.sum()
			
            J_history[i, 0] = self.compute_cost(X, y, theta)
            if i > 1:
                tol = J_history[i-1,0] - J_history[i,0]
            if i % 100 == 0:
                print 'theta:', theta
                print 'cost function:', J_history[i,0]
            
            i = i + 1
        
        self.theta = theta
        return theta, J_history
        
    def predict(self, X):
		""" Make linear prediction based on cost and gradient descent
		:param X: new data to make predictions on
		:return: return prediction
		"""
        prediction = X.dot(theta).flatten()
        return prediction


# initialize linear regression parameters
iterations = 15000
alpha = 0.01
tolerance = 0.00001

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
linearReg = LinReg(alpha = alpha, iterations = iterations, tolerance = tolerance)
theta, J_history = linearReg.gradient_descent(X = it, y = y)

# make a predictions with X = 3.5
print linearReg.predict(np.array([1, 3.5]))