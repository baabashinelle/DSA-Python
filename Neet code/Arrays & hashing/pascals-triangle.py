class Solution(object):
    def generate(self, numRows):
        prev = [[1]]
        for i in range(numRows - 1): # minus one because we've already given the value for the first row
            temp = [0] + prev[-1] + [0] # for every previous row, making it have the "invisible" zero at the beginning and the end and storing it in a temporary value.
            row = [] #an empty row for the next row
            for j in range(len(prev[-1]) + 1): #here we're building the second row. which is the length of the previous row plus one. plus one bc every preceding row is shorter by one than the current row
                row.append(temp[j] + temp[j + 1]) #here we add a current value and the value next to it
            prev.append(row)

        return prev