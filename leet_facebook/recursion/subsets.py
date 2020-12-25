'''
		o=[[]]

1 2 3	o=[[][1]]
i

1 2 3	o=[[][1][2][1,2]]
  i

1 2 3	o=[[][1][2][1,2][3][1,3][2,3][1,2,3]]
    i

https://leetcode.com/problems/subsets/solution/

'''


def subsetElements(nums,n):
    output=[[]]
    for num in nums:
        output+=[cur + [num] for cur in output]
    return output
                

nums = [1,2,3]
print(subsetElements(nums, len(nums)))
