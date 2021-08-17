def reverse_words(string_list):

    ''' 
    Given a list of strings, return a new list where the order is reversed
    '''
    # This reverses the order within the list
    # The list has now been modified
    # Right now just reverses the order of the elements in the list, not the individual string. Ask for help
    changed_words = []

    for string in string_list:
        words = string.split()
        words.reverse()
        changed_words.append(" ".join(words))
    

    return changed_words

if __name__ == "__main__":
    print(reverse_words(["Hello World", "I am here"]))
    # it should print ['World Hello', 'here am I']
