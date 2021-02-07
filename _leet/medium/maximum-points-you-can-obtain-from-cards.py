# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# max sum, pick alternate numbers from both edges
'''
extend given list; for [4,1,5,2], do [4,1,5,2,4,1,5,2]
get sum of last k digits of first half
while i<n, increment i from current position
    remove one element from first half, add one element second half
    compare and keep largest
'''

class Solution:
    def maxScore(self, cardPoints,k):
        if not cardPoints:
            return 0
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        n= len(cardPoints)              #.  0.   1.  2. 3. 4.   5.  6.  7.  8.  9. 10. 11
        cardPoints.extend(cardPoints)   # [100, 40, 17, 9, 73, 75, 100, 40, 17, 9, 73, 75]
        i = n-k
        tot = sum(cardPoints[i: i+k])
        ans = tot

        while i >= n-k and i <= n-1:
            tot += cardPoints[i+k] - cardPoints[i]
            ans = max(ans, tot)
            i += 1

        return ans
        


cardPoints = [100,40,17,9,73,75]

# cardPoints = [1,2,3,4,5,6,1]
k = 3
s=Solution()
print(s.maxScore(cardPoints,k))