# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/


class Solution:
    def findLeastNumOfUniqueInts(self,arr,k):
        ans=0
        from collections import Counter
        count=Counter(arr)
        eliminate=0
        print(count)
        for x in sorted(count.values()):
            if x<=k:
                eliminate+=1
                k-=x
        return len(count)-eliminate


sol=Solution()        
arr = [4,3,1,1,3,3,2]
k = 3
print(sol.findLeastNumOfUniqueInts(arr,k))

'''
Counter({3: 3, 1: 2, 4: 1, 2: 1})
remove 2; now k is 3-1=2
remove 4; now k is 2-1=1
try to remove 1; we cannot because 1 has appeared 2 times
    k=1 i.e., 1<2
    we return number of items we were able to remove
    len(count)-eliminate
'''