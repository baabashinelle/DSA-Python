class Solution(object):
    def replaceElements(self, arr):
        # we set initial max = -1
        # reverse iteration
        # new max =  max(oldmax, arr[i])
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

        # another solution
        # n = len(arr)
        # max_sofar = arr[-1] # start with the last element
        # arr[-1] = -1
        # # Greedily replace the current item with the maximum value sofar
        # for i in range(n-2,-1,-1): # iterative from right to left
        #     cur = arr[i]
        #     arr[i] = max_sofar
        #     max_sofar = max(max_sofar, cur)
        # return arr




        # last = len(arr)-1
        # last = -1
        # for i in range(len(arr)-2):
        #     if arr[i]+1 > i:
        #         i = arr[i] + 1
        #         arr.append(last)
        #         return arr
        # return arr