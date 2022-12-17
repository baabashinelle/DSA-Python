class Solution(object):
    def isSubsequence(self, s, t):
        for letter in s:
            if letter not in t:
                return False

        for letter in s and t:
            if s.index(letter) == t.index(letter):
                return True

        return False