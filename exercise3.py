"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise3
"""
def passwordValidation(password):
    returns = []

    if(len(password) < 8):
        returns.append("Pasword must be at least 8 characters")
    
    digit_count = 0
    capital_count = 0
    special_count = 0

    for i in password:
        if i.isdigit():
            digit_count +=1
        elif i.isupper():
            capital_count +=1
        elif not i.isalnum():
            special_count +=1

    if(digit_count < 2):
        returns.append("The passwordd must contain at least 2 numbers")

    if(capital_count < 1):
        returns.append("password must contain at least one capital letter")

    if(special_count < 1):
        returns.append("password must contain at least one special character")
    
    return {
        "isValid": len(returns) == 0,
        "errors": returns
    }