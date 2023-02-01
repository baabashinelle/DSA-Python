def countdown(number):
    print(number)
    if number == 0: #number == 0 is the base case
        return
    else:
        countdown(number - 1)

number = 10
countdown(number)
