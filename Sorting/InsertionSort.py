def insertion_sort(array):
    for index in range(1, len(array)): # loop begins at index one and runs through array
        temp_value = array[index] # we save the value we are removing in "temp_value"
        position = index - 1 #the value we compare against temp value, which is to the left of the index

    while position >= 0: #runs as long as position is greater or equal to zero
        if array[position] > array[index]: #we then compare by checking if the value at the position is greater than the temp value
            array[position + 1] = array[position] #if it is, we shift that value to the right
            position = position - 1 #We then decrement position by 1 to compare the next left value against the temp_value in the next round of the while loop:
        else: 
            break
    array[position + 1] = temp_value # The final step of each pass-through is moving the temp_value into the gap
    return array #After all pass-throughs have been completed, we return the sorted array