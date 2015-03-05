# Machine-Learning
Various machine learning algorithms broken down in basic and readable python code. Useful for studying and learning how the algorithms function.

* MultiLayerPerceptron.py - Basic multilayer perceptron neural network written with numpy. With weight decay regularization, learning rate decay, softmax or logistic sigmoid output layer, and logistic sigmoid or tanh hidden layer.

* LinearRegression.py - python version of simple linear regression from scratch!

* LogisticRegression.py - gradient descent logistic regression. Currently gets 60% on admission dataset whereas R's default logistic regression gets 70%.

* popcorn.sentiment.sklearn.py - basic sentiment analysis script that converts list of phrases into bag of words features and does logistic regression. Achieved [kaggle](https://www.kaggle.com/c/word2vec-nlp-tutorial/leaderboard) score of .962 and 8th place at the time of writing. 

# Usage

####MultiLayerPerceptron Parameters####
-**iterations (int)**: controls the number of passes over the traning data (aka epochs). Defaults to 50

-**learning_rate (float)**: The learning rate constant controls how much weights are updated on each iteration. Defaults to 0.01.

-**l2_in (float)**: Weight decay regularization term for the input layer weights, keeps weights low to avoid overfitting. Useful when hidden layer is large. Defaults to 0 (off).

-**l2_out (float)**: Weight decay regularization term for the hidden layer weights, keeps weights low to avoid overfitting. Useful when hidden layer is large. Defaults to 0 (off).

-**momentum (float)**: Adds a fraction of the previous weight update to the current weight update. Is used to help system from converging at a local minimum. A high value can increase the learning speed but risks overshooting the minimum. A low momentum can get stuck in a local minimum and decreases the speed of learning. Defaults to 0 (off).

-**rate_decay (float)**: How much to decrease learning rate on each iteration. The idea is to start with a high learning rate to avoid local minima and then slow down as the global minimum is approached. Defaults to 0 (off).

-**output_layer (string)**: Which activation function to use for the output layer. Currently accepts 'logistic' for logistic sigmoid or 'softmax' for softmax. Use softmax when the outputs are mutually exclusive. Defaults to 'logistic'.

-**verbose (bool)**: Whether to print current error rate while training. Defaults to True.