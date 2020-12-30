'''
https://leetcode.com/problems/group-anagrams/

'''



from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
ans=defaultdict(list)
for s in strs:
    ans["".join(sorted(s))].append(s)
print(list(ans.values()))
