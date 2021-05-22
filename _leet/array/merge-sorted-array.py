"""
https://leetcode.com/problems/merge-sorted-array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
d={}
for i in range(m):
    if nums1[i] in d:
        d[nums1[i]]=d[nums1[i]]+1
    else:
        d[nums1[i]]=1
for i in range(n):
    if nums2[i] in d:
        d[nums2[i]]=d[nums2[i]]+1
    else:
        d[nums2[i]]=1
res=[]
for k,v in d.items():
    while v:
        res.append(k)
        v-=1
print(res)
    
    
"""

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1=sorted(nums1[:m]+nums2[:n])
print(nums1[:])
# print(sorted(nums1[:m]+nums2[:n]))

