# The “trick” of using extra function parameters is a common technique in
# writing recursive functions, and a handy one.

#example:

def double_array(array, index): # it accepts two arguments: the array itself, and an index to keep track of
    # Base case: when the index goes past the end of the array
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)

array = [1,2,3,4]
double_array(array, 0)
print(array)


# In each successive call, we pass in the array again as the first argument, but
# we also pass along an incremented index. This allows us to keep track of an
# index just as we would in a classical loop.