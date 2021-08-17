import pickle

def most_common():
    '''
    Function unpickles the shapecolour file and analyses the data for the most common 
    shape-colour pair

    Parameters:
        shapecolour data

    Returns:
        Dictionary with the most common colour and shape pair
    '''
    f = open('shapecolour.p', 'rb')
    data = pickle.load(f)

    # Combine the colour and shape as a new string
    combine = []

    for item in data:
        combine.append(item['colour'] + ' ' + item['shape'])
    
    max = 0

    # Set dictionary to empty values
    common_dict = {
            'Colour' : None,
            'Shape' : None,
        }
    # Loop to find the most common shape-colour pair
    for item in combine:
        if combine.count(item) > max:
            max = combine.count(item)
            x = item.split(' ')
            common_dict = {
                    'Colour' : x[0],
                    'Shape' : x[1],
            }
    
    return common_dict