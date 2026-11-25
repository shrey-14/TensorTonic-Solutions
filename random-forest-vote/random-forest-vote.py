import numpy as np

def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    arr = []
    predictions = np.array(predictions).T
    for i in range(len(predictions)):
        d = {}
        for j in range(len(predictions[i])):
            if predictions[i][j] in d:
                d[predictions[i][j]] += 1
            else:
                d[predictions[i][j]] = 1
        l = list(sorted(d.values(), reverse=True))
        max = l[0]
        keys = []
        for k, v in d.items():
            if d[k] == max:
                keys.append(k)

        keys.sort()
        arr.append(keys[0])

    return arr
        
        
            
    
    