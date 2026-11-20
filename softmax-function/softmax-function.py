import numpy as np
import math

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    arr = []
    for i in range(len(x)):
        if isinstance(x[i], list):
            temp = []
            for j in range(len(x[i])):
                temp.append((math.exp(x[i][j] - np.max(x[i])) / sum([math.exp(ele - np.max(x[i])) for ele in x[i]])))
            arr.append(temp)
        else:
            arr.append((math.exp(x[i] - np.max(x)) / sum([math.exp(ele - np.max(x)) for ele in x])))
            
    return np.array(arr)