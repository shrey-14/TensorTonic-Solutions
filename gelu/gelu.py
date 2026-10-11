import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """

    def gelu(x):
        return ((x / 2) * (1 + math.erf(x / 2**(1/2))))
        
    x = np.asarray(x, dtype=float)
    vectorized_func = np.vectorize(gelu)
    return vectorized_func(x)