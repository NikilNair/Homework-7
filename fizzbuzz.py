def program(val):
    if val % 3 == 0:
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    return(val)

for i in range(1,101):
    print(program(i))
