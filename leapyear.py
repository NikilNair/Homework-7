def program(val):
    if val % 4 != 0:
        return "This is not a leap year"
    elif val % 4 == 0 and val % 100 != 0:
        return "This is a leap year"
    elif val % 4 == 0 and val % 100 == 0 and val % 400 == 0:
        return "This is a leap year"
    elif val % 4 == 0 and val % 100 == 0 and val % 400 != 0:
        return "This is not a leap year"    
