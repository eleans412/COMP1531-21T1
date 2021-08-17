def inverse(d):
    '''
    Given a dictionary d, invert its structure such that values in d map to lists of keys in d.
    For example:
    >>> inverse({1: 'A', 2: 'B', 3: 'A'})
    {'A': [1, 3], 'B': [2]}

    Params:
      d (dict): A dictionary where all the values are hashable (i.e. can be used as keys in the
      result).

    Returns:
      (dict): A dictionary with the structure described above.
    '''
    if type(d) is not dict:
        raise ValueError
    result = {}
    # Loop through all the keys in the input
    for key in d:
        # If this key has not been added to the dictionary, set up an empty list for it
        if d[key] not in result:
            result[d[key]] = []
        result[d[key]].append(key)

    return result
