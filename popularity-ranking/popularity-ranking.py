def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    wr = []
    for i in items:
        weighted_rating = (((i[1] / (i[1] + min_votes)) * i[0]) + ((min_votes / (i[1] + min_votes)) * global_mean))
        wr.append(weighted_rating)

    return wr