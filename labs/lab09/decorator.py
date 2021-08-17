import sys

MESSAGE_LIST = []

def authorise(function):
    """
    You need a function here authorise which contains another function called wrapper.
    This function authenticates the token against CrocodileLikesStrawberries and if valid calls the function given as input,
    authorise then needs to return wrapper.
    """
    # Take in as many arguments as needed
    def wrapper(*args, **kwargs):
        # If token is invalid
        if not authorised(args[0]):
            raise Exception('Invalid token')
        # Gets rid of the token from the arguments list to add them to the message_list
        return function(*args[1:])
    return wrapper
def authorised(auth_token1):
    return auth_token1 == 'CrocodileLikesStrawberries'


@authorise
def get_messages():
    return MESSAGE_LIST

@authorise
def add_messages(msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':
    auth_token = ""
    if len(sys.argv) == 2:
        auth_token = sys.argv[1]
    else:
        auth_token = ""
    #auth_token = 'CrocodileLikesStrawberries'
    add_messages(auth_token, "Hello")
    add_messages(auth_token, "How")
    add_messages(auth_token, "Are")
    add_messages(auth_token, "You?")
    print(get_messages(auth_token))
