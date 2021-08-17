'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A generator that generates the prime factors of n. For example
    >>> list(factors(12))
    [2,2,3]

    Params:
      n (int): The operand

    Yields:
      (int): All the prime factors of n in ascending order.

    Raises:
      ValueError: When n is <= 1.
    '''
    if type(n) is not int or n<=1:
        raise ValueError('Invalid Input')

    # Use the dictionary in divisors to sort through the factors of a number
    # Sort so it is in order
    for fact in sorted(divisors(n)):
        # If n is one do not add this to the list and stop
        # 1 is not a prime factorisation
        if n == 1:
            break
        if is_prime(fact):
            while n != 1 and n % fact == 0:
                yield fact
                n = n // fact