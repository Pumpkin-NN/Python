'''
Multivariate Linear Regression
'''


import numpy as np
import matplotlib.pyplot as plt

def gradient(theta, X):
    vector_m = theta * X
    
    gradient = np.gradient(vector_m)
    plt.plot(gradient)
    # plt.show()
    return gradient
    
def linearRegression(LR, gradient):
    pass


if __name__ == '__main__':
    theta = np.array([80, 5, 3, 2], dtype = float)
    X = np.array([1, 76, 54, 22], dtype = float)
    plt.plot(theta, X)
    plt.show()
    
    
    
    gradient = gradient(theta, X)
    alpha = 0.01
    
    
    
    