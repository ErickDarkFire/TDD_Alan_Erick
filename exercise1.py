"""
Exercise1
"""
def fizzBuzz(num):
    try:
        if num == int(num):
            return str(num)
    except:
        raise ValueError("no es numero")