def program(val):
    if val % 3 == 0:
        return "Fizz"

    return(val)

for i in range(1,101):
    print(program(i))
