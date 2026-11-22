import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    for i in range(len(x)):
        x[i] = x[i] if x[i] >= 0 else alpha*x[i]
    return np.array(x)