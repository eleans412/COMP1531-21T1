import sys

def roman(numerals):
    '''
    Given Roman numerals as a string, return their value as an integer. You may
    assume the Roman numerals are in the "standard" form, i.e. any digits
    involving 4 and 9 will always appear in the subtractive form.

    For example:
    >>> roman("II")
    2
    >>> roman("IV")
    4
    >>> roman("IX")
    9
    >>> roman("XIX")
    19
    >>> roman("XX")
    20
    >>> roman("MDCCLXXVI")
    1776
    >>> roman("MMXIX")
    2019
    '''
    roman_val = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    
    # Check for invalid input
    # If empty string
    if numerals == '':
        raise Exception('Not valid input')

    ix = 0
    result = 0
    # Loop through to check roman numerals and add value if found relevant characters
    while ix < len(numerals):
        for k, v in roman_val:
            # Looks for roman numerals of the same length and type of a number.
            # e.g Excludes IX for I
            if numerals.startswith(k, ix):
                result += v
                ix += len(k)
                break
        else:
            raise Exception('Invalid Roman number.')
    
    return result


