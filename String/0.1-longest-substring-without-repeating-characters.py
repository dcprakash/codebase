'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
sliding window
same concept as minimum-window-substring
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	chars = [0]*128
    	
    	left = right = 0
    	
    	res=0
    	while right<len(s):
    		r=s[right]
    		chars[ord(r)]+=1
    		
    		while chars[ord(r)] > 1:
    			l=s[left]
    			chars[ord(l)]-=1
    			left+=1
    		
    		res=max(res, right-left+1)
    		right+=1
    	
    	return res
    	