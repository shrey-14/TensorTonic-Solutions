import math

def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    # Write code here
    lower_bound = ((len(values) - 1) * lower_pct) / 100
    upper_bound = ((len(values) - 1) * upper_pct) / 100

    ql = values[math.floor(lower_bound)] + (lower_bound - math.floor(lower_bound))*(values[math.ceil(lower_bound)] - values[math.floor(lower_bound)])

    qu = values[math.floor(upper_bound)] + (upper_bound - math.floor(upper_bound))*(values[math.ceil(upper_bound)] - values[math.floor(upper_bound)])

    for i in range(len(values)):
        if values[i] < ql:
            values[i] = ql
        elif values[i] > qu:
            values[i] = qu

    return values