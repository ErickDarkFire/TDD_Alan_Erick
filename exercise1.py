"""
Exercise1
"""
def fizzBuzz(num):
    try:
        if num % 3 == 0:
            return "Fizz"
        elif num == int(num):
            return str(num)
    except:
        raise ValueError("no es numero")