"""
Exercise3
"""
def passwordValidation(password):
    returns = []

    if(len(password) < 8):
        returns.append("Pasword must be at least 8 characters")
    
    return {
        "isValid": len(returns) == 0,
        "errors": returns
    }