from math import sqrt
def divisors(n):
    '''
    Given some number n, return a set of all the numbers that divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    # Check the input
    if type(n) is not int or n <= 0:
        raise ValueError('Invalid input')

    # Add the case that the number is divisible by 1 and itself
    divisors_dict = {n}
    i = 1
    # Because everything higher than this will just be repeated divisors
    while i < sqrt(n)+1:
        if n % i == 0:
            divisors_dict.add(i)
            divisors_dict.add(n//i)
        i += 1
    # Add n to the list because n is divisible by itself
    # If you were to add this in order you would have to sort the values

    return divisors_dict
