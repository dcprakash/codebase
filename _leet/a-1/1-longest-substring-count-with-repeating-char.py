'''
https://leetcode.com/problems/longest-repeating-character-replacement/

1-longest-substring-count-without-repeating-char.py
O(26*n)=O(n)
'''

class Solution:
    def characterReplacement(self, s, k):

        chars = [0] * 128    #because there are 26 uppercase english chars
        left = right = 0
        res = 0
        maxfreq = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            maxfreq = max(maxfreq, chars[ord(r)])     # to get length of most frequent char, in given window we would want to replace char that appears less
                                                      # no need to decrement maxfreq when chars[ord(l)] -= 1 because we only care about maximizing the results
            if (right-left+1)-maxfreq>k:   # in given window length - most frequent chars = chars that are less frequent; if less frequent char > k, we need to find another window that fits size
                l = s[left]                # in given window len i.e., right-left+1, remove max frequent chars; if remaining is still > k then we have to reduce window. there are too many repeating chars that cannot be replaced by k
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
            
        return res


s=Solution()
print(s.characterReplacement("ABAB",2))

'''
0123
ABAB
when right=3, left=0
maxfreq 2 (bcz A and B appeared twice)
res=3

(3-1+1)-2>2: this is for ABAB
    no

if we had ABCAB, then in given window ABCA we would see there are more than K characters to replace

'''