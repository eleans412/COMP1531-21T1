import random

def multiply():
    '''
    Program tests the user's knowledge of timetables
    Generates numbers to be multiplied and asks for user input until correct answer
    is given

    Parametres:
        None

    Returns: 
        (bool) true if correct
    '''
    num1 = random.randrange(2,12)
    num2 = random.randrange(2,12)
    correct_ans = num1 * num2

    correct = False
    while correct == False:
        user_ans = int(input(f"What is {num1} x {num2}? "))
        if user_ans == correct_ans:
            correct = True
        else:
            print('Incorrect - try again.')

    if correct == True:
        print('Correct!')

multiply()
