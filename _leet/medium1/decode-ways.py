'''
Excel column number to name
https://leetcode.com/problems/decode-ways/

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

18
18 -> AH
18 -> R 
2 ways

there is no alphabet matching 0
20->T
60->cannot decode

909
9,90 (cannot decode 90 no alphabet)
90(cannot decode 90 no alphabet), 9
9,0(cannot decode 0 no alphabet),9
0 ways

keep map to store memory of characters already processed
as we can see below, 25 can be just processed once and used in many places
                    2125
            2 125           21 25
          1 25  12 5      2 5   25
          

15
dp=[1 2]
1 can be decoded in one way
5 can be decoded as 5
15  is also valid

      2 1 2 5
dp=[0 0 0 0 0]
dp=[1 1 0 0 0]
first index is always 1
second index is if value is non zero
dp=[1 1 2 0 0]
1 can be decoded as 1 and 21, so 2 ways
dp=[1 1 2 3 0]
2 can be decoded as, 2, 21, 22 so 3 ways
dp=[1 1 2 3 0]
25, 15, 25, 5 so 4 ways
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # Array to store the subproblem results
        # plus 1 to include emptry string possibility
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        # iterate from 2nd charcter of string, we have already computed first char above
        for i in range(2, len(dp)):
            # if previous char is 0, we cannot have valid single digit
            # Check if successful single digit decode is possible.
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        

s=Solution()
print(s.numDecodings("18"))


'''
                                Algorithm

If the string s is empty or null we return the result as 0.

Initialize dp array. dp[0] = 1 to provide the baton to be passed.

If the first character of the string is zero then no decode is possible hence initialize dp[1] to 0, otherwise the first character is valid to pass on the baton, dp[1] = 1.

Iterate the dp array starting at index 2. The index i of dp is the i-th character of the string s, that is character at index i-1 of s.

We check if valid single digit decode is possible. This just means the character at index s[i-1] is non-zero. Since we do not have a decoding for zero. If the valid single digit decoding is possible then we add dp[i-1] to dp[i]. Since all the ways up to (i-1)-th character now lead up to i-th character too.

We check if valid two digit decode is possible. This means the substring s[i-2]s[i-1] is between 10 to 26. If the valid two digit decoding is possible then we add dp[i-2] to dp[i].

Once we reach the end of the dp array we would have the number of ways of decoding string s
'''