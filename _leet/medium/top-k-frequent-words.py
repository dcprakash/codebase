# top k frequent words
# https://leetcode.com/problems/top-k-frequent-words/
# frequency


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
    
    
def topKFrequentEfficient(words, k):
    from collections import Counter
    count=Counter(words)
    candidates=count.keys()
    candidates.sort(key=lambda w: (-count[w], w))
    return candidates[:k]
    
# Counter({'the': 4, 'is': 3, 'sunny': 2, 'day': 1})
inputs = ["the", "day", "is", "sunny", "rome", "the", "the", "the", "sunny", "is", "is", "rome"]
k=4
print(topKFrequent(inputs, k))
print(topKFrequentEfficient(inputs, k))


    

    