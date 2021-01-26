# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# max sum, pick alternate numbers from both edges


class Solution:
    def maxScore(self, cardPoints,k):
        if not cardPoints:
            return 0
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        n= len(cardPoints)
        cardPoints.extend(cardPoints)
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