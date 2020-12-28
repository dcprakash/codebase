"""
https://leetcode.com/problems/container-with-most-water/solution/

"""


def maxWater(height):
    area=0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area=max(area, min(height[i],height[j]) * (j-i))
    return area


def maxWaterEfficient(height):
    area=0
    l=0
    r=len(height)-1
    while l<r:
        area = max(area, min(height[l], height[r]) * (r-l))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return area


w=[4,3,2,1,4]
print(maxWater(w))
# print(maxWaterEfficient(w))