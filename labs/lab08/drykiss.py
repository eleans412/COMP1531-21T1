from functools import reduce
import operator

def drykiss(my_list):
    min_num = min(my_list)
    first_prod = reduce(operator.mul, my_list[0:4], 1)
    last_prod = reduce(operator.mul, my_list[1:5], 1)
    result = (min_num, first_prod, last_prod)
    return result

if __name__ == '__main__':
    # Automate the repeted code in a for loop to request the user 
    # to enter in a, b, c, d, e
    letter_list = ['a', 'b', 'c', 'd', 'e']
    inputs = []
    for i in range(len(letter_list)):
        user_input = int(input(f'Enter {letter_list[i]}: '))
        inputs.append(user_input)

    # Send lists to dry kiss so that tuple is formed for drykiss tests
    result = drykiss(inputs)
    # Print the minimum of the ints in the list of inputs
    print("Minimum: " + str(result[0]))
    print("Product of first 4 numbers: ")
    print(result[1])
    print("Product of last 4 numbers")
    print(result[2])
