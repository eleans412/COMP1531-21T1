
def permutations(string):
    '''
    For the given string, compute the set of all permutations of the characters of that string. For example:
    >>> permutations('ABC')
    {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

    Params:
      string (str): The string to permute

    Returns:
      (set of str): Each string in this set should be a permutation of the input string.
    '''
    if len(string) == 1:
        return {string}
    
    str_list = []
    for char in string:
        for perm in permutations(string.replace(char, '', 1)):
            str_list.append(char + perm)

    return set(str_list)
