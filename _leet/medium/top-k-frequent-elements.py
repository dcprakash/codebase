# top k frequent numbers
# https://leetcode.com/problems/top-k-frequent-elements/
    
    
def topKFrequentEfficient(nums, k):
    from collections import Counter
    count=Counter(nums)
    # candidates=count.keys() # works in python 2
    candidates=list(count.keys())
    candidates.sort(key=lambda w: (-count[w]))
    return candidates[:k]
    

nums = [1,4,4,5,5,5]
k = 2
print(topKFrequentEfficient(nums, k))


    

    