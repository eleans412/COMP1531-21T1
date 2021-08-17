import typing

def multiply_by_two(number: (int, float)):
    '''
    Multiplies a given number by two.
    '''
    number = int(number)
    return (number * 2)

def print_message(message: str):
    '''
    Returns a given message.
    '''
    return message

def sum_list_of_numbers(numbers: (list, int, float)):
    '''
    Returns the sum of a list of numbers
    '''
    result = 0

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        result = result + numbers[i]
        i += 1

    return result
    

def sum_iterable_of_numbers(numbers: (list, dict, tuple, int, float)):
    '''
    Calculates the sum of an iterable of numbers

    numbers: any iterable

    Return value: integer
    '''
    result = 0

    # If a single number
    if len(numbers) == 1:
        result = int(numbers[0])
    # If there is more than one number in the iterable
    else:
        converted_numbers = [int(i) for i in numbers]
        #for i in range(len(numbers)):
            #numbers[i] = int(numbers[i])
            #i += 1
        result = sum(converted_numbers)

    return result

def is_in(needle : (str, int), haystack: (list, str, int)):
    '''
    Checks if the given item is in a list

    Parameters:
    - needle: a string or an integer
    - haystack: a list of strings or integers

    Return value: bool - if the needle is in the haystack
    '''

    found = False

    for search in haystack:
        if search == needle:
            found = True

    return found

def index_of_number(item: int, numbers: (list)):
    '''
    Returns the index of the given item in a list of numbers

    Parameters:
    - item: an integer
    - numbers: a list of numbers

    Return value: the index of the item, or None if the items is not in numbers
    '''
    idx = None
    i = 0
    item = int(item)

    # To ask - the tests have been written where item corresponds to a list
    # Do I change the order or is there another way to go about this
    # Same as the above function in tests
    while i < len(numbers):
        converted_numbers = [int(i) for i in numbers]

        if converted_numbers[i] == item:
            idx = i
        i += 1
    return idx 

