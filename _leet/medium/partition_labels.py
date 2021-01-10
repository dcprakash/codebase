'''
https://leetcode.com/problems/partition-labels/submissions/

For each letter encountered, process the last occurrence of that letter, 
    extending the current partition 
For "abccaddbeffe", the minimum first partition is "abccaddb" 
    (c and d are not beyond this output)
    
We need an array last[char] -> index of S where char occurs last. 
Then, let anchor and j be the start and end of the current partition.


'''


def partitionLabels(S):
    # overwrite index (i) of char (c) into dict (last), where key is char (c)
    last = {c: i for i, c in enumerate(S)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
            
    return ans
        
#    0123456789 
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
