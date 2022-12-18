class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for i,n in enumerate(nums):
            another = target - n
            if another in numMap:
                return [numMap[another], i]
            numMap[n] = i
                
        return
