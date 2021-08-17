import math
from itertools import groupby

# Check for inconsistencies in size of input
def is_square(square):
    '''
    Checks if the input is a square, not missing any input in its respective list

    Parameters:
        Square (Nested list): Is the matrix to be checked

    Returns:
        (bool): true if the square is valid input and false if not
    '''
    for i in range(len(square)):
        if len(square[i]) != len(square):
            return False
    return True

def is_repeat(square):
    '''
    Checks if there are repeated numbers in the matrix given

    Parameters:
        Square (Nested list): Is the matrix to be checked

    Returns:
        (bool): true if the square is valid input and false if not
    '''
    g = groupby(square)
    return next(g, True) and not next(g, False)



def magic(square):
    '''
    Checks if the matrix input is a magic square

    Parameters:
        Square (Nested list): Is the matrix to be checked

    Returns:
        Statement as to if the matrix is a magic square
    '''
    # Check for missing or invalid data
    if(not(is_square(square))): 
        return 'Invalid data: missing or repeated number'

    if(is_repeat(square)):
        return 'Invalid data: missing or repeated number'

    # Calculate if magic square
    # if not 15, not magic square
    # Calculate along the diagonals
    total = 0
    x = len(square)
    for i in range(x):
        total += square[i][i]
    
    if not(math.isclose(total, x*(x * x + 1)/2)):
        return 'Not a magic square'
    
    # Calculate along the diagonals
    total = 0
    for i in range(x):
        total += square[i][x-1-i]

    if not(math.isclose(total, x*(x * x + 1)/2)):
        return 'Not a magic square'

    # Check rows are 15
    for i in range(x):
        total = 0
        for j in range(x):
            total += square[i][j]
        if not(math.isclose(total, x*(x * x + 1)/2)):
            return 'Not a magic square'

    # Check columns are 15
    for i in range(x):
        total = 0
        for j in range(x):
            total += square[j][i]
        if not(math.isclose(total, x*(x * x + 1)/2)):
            return 'Not a magic square'

    return 'Magic square'
