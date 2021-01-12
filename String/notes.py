# top k frequent numbers
# https://leetcode.com/problems/top-k-frequent-words/

def topKFrequent(words, k):
    d={}
    for i in inputs:
        if i in d:  d[i]+=1
        else:   d[i]=1
    # print(sorted(d.items(), key=lambda item: (item[1],len(item[0])), reverse=True))
    
    res=[]
    c=0
    for key,val in sorted(d.items(), key=lambda item: (-item[1], item[0])):
        if c<k:
            res.append(key)
            c+=1
    return res
    
    
def topKFrequentEfficient(nums, k):
    from collections import Counter
    count=Counter(nums)
    # candidates=count.keys()
    candidates=list(count.keys())
    candidates.sort(key=lambda w: (-count[w]))
    return candidates[:k]
    
# Counter({'the': 4, 'is': 3, 'sunny': 2, 'day': 1})
nums = [1,4,4,5,5,5]
k = 2
# print(topKFrequent(nums, k))
print(topKFrequentEfficient(nums, k))


    

    