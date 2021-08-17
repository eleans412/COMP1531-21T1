def reduce(f, xs):
    # If there is nothing in the list
    if not xs:
        return None
    # If there is only one item in the list - return that item
    elif len(xs) == 1:
        return xs[0]
    # Else, send it to the f function
    # Get the  return value from the function f and the next value from the list back 
    # in to the function f and repeats until the list xs is empty
    else:
        return f(reduce(f, xs[:-1]), xs[-1])


if __name__ == '__main__':
    print(reduce(lambda x, y: x + y, [1,2,3,4,5]))
    print(reduce(lambda x, y: x * y, [1,2,3,4,5]))