# top k frequent numbers
# https://leetcode.com/problems/top-k-frequent-elements/
# list comp
    
    
def topKFrequentEfficient(nums, k):
    from collections import Counter
    count=Counter(nums)     # Counter({4: 3, 5: 2, 2: 1})
    candidates=list(count.keys())   # [2, 4, 5]
    # reverse sort keys based on repeated counter values
    candidates.sort(key=lambda w: (-count[w]))  # [4, 5, 2]
    return candidates[:k]   # return upto k elements
    

nums = [2,4,4,4,5,5]
k = 2
print(topKFrequentEfficient(nums, k))


    

    