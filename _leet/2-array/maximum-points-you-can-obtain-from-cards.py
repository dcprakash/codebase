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
        
        n= len(cardPoints)  
        tot=sum(cardPoints[n-k:n])
        ans = tot
        cardPoints.extend(cardPoints)   # [1,2,3,4,5,6,1, 1,2,3,4,5,6,1]
        i = n-k

        while i >= n-k and i <= n-1:    # b.w last k chars of n index
            tot += cardPoints[i+k] - cardPoints[i]
            ans = max(ans, tot)
            # tot=ans     # if question ask to choose any card from last and first 3
            i += 1
            # k-=1        # if question ask to choose any card from last and first 3

        return ans
    

# cardPoints = [100,40,17,9,73,75]
# cardPoints = [100,200,400,5,6,310,300,50]

cardPoints = [1,2,3,4,5,6,1]
k = 3
s=Solution()
print(s.maxScore(cardPoints,k))
