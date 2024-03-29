
# https://leetcode.com/problems/jump-game/
# steps
# https://www.youtube.com/watch?v=2HnlGToCdCc&feature=emb_logo&ab_channel=TerribleWhiteboard
'''
 0
[4,_,_,_,_]
can you get from 0th index to end of array?
enf of arry is 4 places further
from 0th index + 4 steps = end of array
'''

def canJump(nums):
    lastValidIndex=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if (i+nums[i] >= lastValidIndex):
            lastValidIndex = i
    return lastValidIndex==0


#       0 1 2 3 4
nums = [2,3,1,1,4]
# nums = [2, 0, 0]
# nums = [3,2,1,0,4]
print(canJump(nums))

'''
 0 1 2 3 4
[2,3,1,1,4]
[2,0,0]
'''