import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    v = np.array(v)
    w = np.array(w)
    num = (np.dot(v, w)) 
    deno = ((sum([e1**2 for e1 in v])**0.5) * (sum([e2**2 for e2 in w])**0.5)) 
    if deno == 0:
        return np.nan
    return float(np.arccos(np.clip(num / deno, -1, 1)))