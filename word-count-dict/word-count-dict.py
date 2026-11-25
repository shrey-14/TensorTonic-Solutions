def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d