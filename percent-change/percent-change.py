def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here
    ca = []
    for i in range(1,len(series)):
        ca.append((0.0 if series[i-1] == 0 else (series[i] - series[i-1]) / series[i-1]))

    return ca