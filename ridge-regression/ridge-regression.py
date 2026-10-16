import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    I = np.identity(X.shape[1])

    return np.linalg.inv(X.T @ X + lam * I) @ X.T @ y
    