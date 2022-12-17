class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return None
            
        l = s.split()
        return len(l[-1])