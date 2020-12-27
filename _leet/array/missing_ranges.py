'''
https://leetcode.com/problems/missing-ranges/solution/
'''

def helper(low, up):
    return str(low) if low==up else str(low) + "->" + str(up)
    

def getRange(nums, n, lower, upper):
    res=[]
    prv=lower-1
    for i in range(n+1):
        cur=nums[i] if i<n else upper+1
        if prv+1<=cur-1:
            res.append(helper(prv+1, cur-1))
        prv=cur
    return res
        

nums = [0,1,3,50,75]
lower = 0
upper = 99
print(getRange(nums, len(nums), lower, upper))

# Output: ["2","4->49","51->74","76->99"]