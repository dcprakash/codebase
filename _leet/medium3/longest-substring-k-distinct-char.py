'''

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/

return "longest" substring that
should NOT have more than k distinct characters

- Return 0 if the string is empty or k is equal to zero.
- Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1.
- While right pointer is less than N:
    Add the current character s[right] in the hashmap and move right pointer to the right.
    If hashmap contains k + 1 distinct characters, remove the leftmost character from the hashmap and move the left pointer so that sliding window contains again k distinct characters only.
    Update max_len.

sliding window

'''
from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        if n * k == 0:  return 0
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1     # min would be 1, bcz we already returned 0 if its empty string
        
        while right<n:
            hashmap[s[right]]=right
            right+=1
            
            if len(hashmap)==k+1:   # we only need k distinct char, if reached then evaluate
                # delete the character with most distinct value
                del_idx = min(hashmap.values())
                # remove from hashmap (no need to remove from actual string)
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)
        # print(hashmap)    # {'b': 3, 'a': 4}
        
        return max_len


s=Solution()
print(s.lengthOfLongestSubstringKDistinct("eceba", 2))
