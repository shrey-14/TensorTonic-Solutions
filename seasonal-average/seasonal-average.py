def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here
    d = {}
    for i in range(len(series)):
        if i % period in d:
            d[i % period].append(series[i])
        else:
            d[i % period] = []
            d[i % period].append(series[i])
            
    for k, v in d.items():
        d[k] = sum(v)/len(v)
    
    return list(d.values())
    