import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    q = []
    for i in range(len(predictions)):
        if i == target:
            q.append((1 - epsilon) + (epsilon / len(predictions)))
        else:
            q.append((epsilon / len(predictions)))

    return -1 * sum([(qi * math.log(pi)) for qi, pi in zip(q, predictions)])
        
        