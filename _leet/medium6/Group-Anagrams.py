'''
https://leetcode.com/problems/group-anagrams/

anagrams
Group-Anagrams

when we sort the string, while adding to dictionary, we keep appending to same key; with actual unsorted values

'''



from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
ans=defaultdict(list)
for s in strs:
    ans["".join(sorted(s))].append(s)
print(list(ans.values()))
