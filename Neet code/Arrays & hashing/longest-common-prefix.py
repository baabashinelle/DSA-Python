class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: #comaring an arbitrary string to the first character in the first string
                    return res
            res += strs[0][i]

        return res