def factorial(number):
    if number == 1: #base case
        return 1
    else:
        return number * factorial(number - 1) #factorial(number - 1) is the subproblem