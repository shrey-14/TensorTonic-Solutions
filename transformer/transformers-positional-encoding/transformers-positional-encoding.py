import numpy as np
import math

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Returns the sinusoidal position matrix.
    """
    arr = []
    for i in range(seq_length):
        l = []
        for j in range(0, d_model, 2):
            l.append(math.sin(i/(10000**((j)/d_model))))
            l.append(math.cos(i/(10000**((j)/d_model))))
        arr.append(l)
    return np.array(arr)