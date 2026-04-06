"""
Exercise1
"""
def fizzBuzz(num):
    try:
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        elif num == int(num):
            return str(num)
    except:
        raise ValueError("no es numero")