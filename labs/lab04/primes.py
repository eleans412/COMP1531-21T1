import math

def factors(num):
    '''
    Returns a list containing the prime factors of 'num'. The primes should be
    listed in ascending order.

    For example:
    >>> factors(16)
    [2, 2, 2, 2]
    >>> factors(21)
    [3, 7]

    Parameters:
        None

    Returns:
        prime_factors (List): list of prime factors of num
    '''
    # Check if num is a negative number
    # Raise error if so
    if num < 1:
        raise Exception('Invalid input. Number cannot be less than 1')


    # Set an empty list to be filled with prime factors
    prime_factors = []
    
    # Prime numbers starting from 2
    d = 2
    # Only enter while loop if multiples of 2 as a prime is less than num
    # As 2 * 2 = 4. Anything greater than 4 will have prime factors
    while d * d <= num:
        # Add to the prime_factors list if the num is divisible by d
        while (num % d) == 0:
            prime_factors.append(d)
            # Reduce the num by d to see if there are any other prime factors of nums
            num //=d
        d += 1
    # Otherwise if num is greater than 1 and 1 only, then append to the list
    if num > 1:
        prime_factors.append(num)


    return prime_factors
