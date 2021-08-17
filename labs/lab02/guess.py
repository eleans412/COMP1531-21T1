
#def guess_num():
# Set limits
upper_limit = 100
lower_limit = 1
print("Pick a number between 1 and 100 (inclusive)")

am_correct = False

# Loop until correct
while am_correct == False:
    guess = round((lower_limit + upper_limit)/2)
    print("My guess is:", guess)
    print("Is my guess too low (L), too high (H), or correct (C)?")
    user_input = input()
    
    # If too low
    if user_input == "L":
        lower_limit = guess + 1
    # If too high
    elif user_input == "H":
        upper_limit = guess - 1
    # If input not L, H or C
    elif "L" and "H" and "C" not in user_input:
        continue
    # If correct
    elif user_input == "C":
        am_correct = True


print("Got it!")


#guess_num

#if __name__ == "__main__"
