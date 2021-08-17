def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
 
 

    # Count length of password
    length = len(password)

    number = False
    upper_case = False
    lower_case = False

    
    # Check for specific characters
    for char in password:
        if char.isdigit():
            number = True
        elif char.isupper():
            upper_case = True
        elif char.islower:
            lower_case = True
    
     # If horrible password
    if password == "password" or password == "iloveyou" or password == "123456":
        return "Horrible Password"    
    # Check the length of the password
    elif length >= 8 and number:
        if length >= 12 and upper_case and lower_case:
            return "Strong Password"
        else:
            return "Moderate Password"
    else:  
        return "Poor Password"
    

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do?
