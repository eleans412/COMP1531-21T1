
def neighbours(iterable):
    '''
    A generator, that, given an iterable, yields the "neighbourhood" of each
    element. The neighbourhood is a tuple containing the element itself as well
    as the one that comes before and the one that comes after. For example,
    >>> list(neighbours([1,2,3,4]))
    [(1,2), (1,2,3), (2,3,4), (3,4)]

    Note that the first and last elements are pairs, while the rest are triples.

    Params:
      iterable (iterable): The iterable being processed. In the event it's empty,
      this generator should not yield anything. In the event it only contains
      one element, only that element should be yielded in a one-tuple.

    Yields:
      (tuple) : The neighbourhood of the current element.
    '''
    # Hint: Don't forget that iterables can produce values infinitely. You can't
    # rely on being able to retrieve all the elements at once.
    
    # Look at the first number - get the number in front of it (i.e, its neighbourhood)
    # Yield that as a pair tuple

    # Look at the succeeding numbers - yield their neighbourhood
    nxt = iter(iterable)
    current = tuple()
    try:
        # Check that there is an element after the current on on the iterable
        # Format it to be a tuple of the necessary type
        current = current + (next(nxt),)
    # If the next is a none type (i.e. the end of the iterable) then return
    except StopIteration:
        return
    # Keep iterating and yielding until there are no more inputs to get the neighbourhood for in the iterable
    try:
        while True:
            current = current + (next(nxt),)
            yield current
            if len(current) == 3:
                # If the length of the current tuple is 3 (i.e. not the first or last number, add it after the first tuple)
                current = current[1:]
    # If there is no next input after the last number, then yield the final input
    except StopIteration:
        yield current