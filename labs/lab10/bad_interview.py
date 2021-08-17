def bad_interview():
    '''
    A generator that yields all numbers from 1 onward, but with some exceptions:
    * For numbers divisible by 3 it instead yields "Fizz"
    * For numbers divisible by 5 it instead yields "Buzz"
    * For numbers divisible by both 3 and 5 it instead yields "FizzBuzz"
    '''
    i = 1
    # Keep looping from 1
    while True:
        # If divisible by 3 and 5 yield and move onto the next number
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
            i+=1
        # If divisible by just 3 yield and move onto the next number
        if i % 3 == 0:
            yield "Fizz"
            i+=1
        # If divisible by just 5 yield and move onto the next number
        if i % 5 == 0:
            yield "Buzz"
            i+=1
        # If not satisifying the above conditions, just yield the number
        else:
            yield i
            i+=1
    
