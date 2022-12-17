class Solution(object):
    def containsDuplicate(self, nums):
        # using dictionary
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        for n in count.values():
            if n > 1:
                return True

            return False

        # using set
        return len(nums) != len(set(nums))