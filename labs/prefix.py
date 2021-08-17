def prefix_search(dictionary, key_prefix):
    '''
    Given a dictionary (with strings for keys) and a string, returns a new dictionary containing only the keys (and their corresponding values) for which the string is a prefix.
    If the string is not a prefix for any key, a KeyError is raised.
    You can assume that you will not be given any empty strings in dictionary or as key_prefix

    For example,
    >>> prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a")
    {'ac': 1, 'ab': 3}
    '''

    new_dict = {}
    character_count = 0

    # Count the number of characters in the key prefix
    # Assumed that Key_prefix should only be one character
    for characters in key_prefix:
        character_count += 1

    if character_count == 1:
        # Check for keys with the necessary prefix
        for key in dictionary:
            if key.startswith(key_prefix):
                new_dict[key] = dictionary[key]
            # If key_prefix not found, raise KeyError

        # Check if new_dictionary is empty
        if bool(new_dict):
            return new_dict
        else:
            # After loop if new_dict is empty then raise Key Error
            raise KeyError("Key not valid")        


    return dictionary
