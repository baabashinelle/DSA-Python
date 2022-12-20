from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        letters = defaultdict(list) #mapping the character count of each string to a list of anagrams
        # go through each string to count the number of characters in each string
        for s in strs:
            count = [0] * 26 #a...z

            for c in s: 
                #go through every character in each string
                count[ord(c) - ord("a")] += 1 # subtracting the ASCII value of a from the ASCII value of "a"

            letters[tuple(count)].append(s) # append the string of that particular count to the list

        return letters.values()