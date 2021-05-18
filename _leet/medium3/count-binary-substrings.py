'''
https://leetcode.com/problems/count-binary-substrings/

array groups that represents the length of same-character contiguous blocks
s = "110001111000000", then groups = [2, 3, 4, 6]
11,000,1111,000000

If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000"
ans = min(groups[i], groups[i+1])


01234   index
10101   then groups = [1, 1, 1, 1, 1]

01234567
00110011    groups=[2,2,2,2]

'''

class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
        
obj=Solution()
# print(obj.countBinarySubstrings("10101"))
print(obj.countBinarySubstrings("00110011"))
