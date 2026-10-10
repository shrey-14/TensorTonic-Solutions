import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    kernel = []
    sum = 0
    centre = size // 2
    for i in range(size):
        dx = i - centre
        l = []
        for j in range(size):
            dy = j - centre
            g = math.exp(-((dx**2 + dy**2) / (2 * sigma**2)))
            sum += g
            l.append(g)
        kernel.append(l)

    for i in range(size):
        for j in range(size):
            kernel[i][j] = kernel[i][j] / sum
            
    return kernel