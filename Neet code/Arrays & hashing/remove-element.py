class Solution(object):
    def removeElement(self, nums, val):
        k = 0 # initialize this pointer to index zero
        for i in range(len(nums)):
            if nums[i] != val:
                # partition / swap
                nums[k] = nums[i]
                k += 1
        return k