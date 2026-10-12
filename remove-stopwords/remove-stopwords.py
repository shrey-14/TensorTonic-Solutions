def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    i = 0
    while i < len(tokens):
        if tokens[i] in stopwords:
            tokens.pop(i)
        else:
            i += 1

    return tokens