def divide(n1,  n2):
    try:
        return n1 / n2
    except (ValueError, TypeError):
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"    
        
    
print(divide(22, 0x99))
