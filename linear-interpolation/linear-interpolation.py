def linear_interpolation(values: list) -> list:
    """
    Returns a copy with every missing value interpolated.
    """
    # Write code here
    for i in range(len(values)):
        if values[i] == None:
            v_left = values[i-1]
            right, v_right = -1, -1
            for j, ele in enumerate(values[i+1:]):
                if ele != None:
                    right, v_right = i+1+j, ele
                    break
            
            values[i] = v_left + (((i - (i-1))/(right - (i-1))) * (v_right - v_left))

    return values
            