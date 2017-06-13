def fizz_buzz(number):
    """This function tests for the numbers divisible by 3 or 5 and by both, then returns respective outputs"""
    if type(number)!=int:
        raise TypeError
    else:
        if number%15==0:
            return 'FizzBuzz'
        elif number%3==0:
            return 'Fizz'
        elif number%5==0:
            return 'Buzz'
        else:
            return number