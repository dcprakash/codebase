'''
https://leetcode.com/problems/find-common-characters/

# We can first find all the distinct letters that exist in A
# For each distinct letter, we find how many times it occurs in each word in A. Take the minimum occurance.
# occurance gives you something like this [["e",1],["a",0],["l",2],["r",0],["o",0],["b",0]]
# This indicates we need to append 'e' 1 time, and 'l' 2 times. Other letters did not occur in some words since their minimum occurance is 0.

common characters
duplicate characters
 
'''

class Solution:
    def commonChars(self, words):
        letters = set([char for word in words for char in word])    # {'b', 'l', 'e', 'r', 'a', 'o'}
        occurance = [[l, min([w.count(l) for w in words])] for l in letters]    # [['e', 1], ['l', 2], ['r', 0], ['o', 0], ['a', 0], ['b', 0]]
        ans = []
        for o in occurance:
            ans+=o[0]*o[1]
        return ans
        
        
obj=Solution()
print(obj.commonChars(["bella","label","roller"]))

