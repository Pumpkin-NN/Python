import numpy as np
import matplotlib.pyplot as plt






if __name__ == "__main__":
    
    #Genarate Data
    true_slope = 10.889
    true_intercept = 3.456
    input_var = np.arange(0.0,100.0)
    output_var = true_slope * input_var + true_intercept + 500.0 * np.random.rand(len(input_var))
    
    # Plot the datas
    plt.scatter(input_var, output_var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    