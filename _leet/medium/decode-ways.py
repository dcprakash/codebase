'''
Excel column number to name
https://leetcode.com/problems/decode-ways/

18
18 -> AH
18 -> R 
2 ways

909
9,90 (cannot decode 90 no alphabet)
90(cannot decode 90 no alphabet), 9
9,0(cannot decode 0 no alphabet),9
0 ways

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
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


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
print(s.numDecodings("123"))


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