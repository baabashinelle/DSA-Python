def factorial(number):
    if number == 1: #base case
        return 1
    else:
        return number * factorial(number - 1) #factorial(number - 1) is the subproblem



# Bottom up strategy using the trick of passing extra parameters
# def factorial(n, i=1, product=1):
#     return product if i > n
#     return factorial(n, i + 1, product * i)
# end