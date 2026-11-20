import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    variance = sum([(ele - np.mean(x))**2 for ele in x]) * (1/(len(x) - 1))
    return {'variance': float(variance), 'standard_deviation': float(variance ** 0.5)}