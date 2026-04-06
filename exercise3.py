"""
Exercise3
"""
def passwordValidation(password):
    returns = []

    if(len(password) < 8):
        returns.append("Pasword must be at least 8 characters")
    
    digit_count = 0

    for i in password:
        if i.isdigit():
            digit_count +=1

    if(digit_count < 2):
        returns.append("The passwordd must contain at least 2 numbers")
        
    return {
        "isValid": len(returns) == 0,
        "errors": returns
    }