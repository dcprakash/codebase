'''
https://leetcode.com/problems/longest-common-prefix/

longest prefix
longest common prefix

zip is used for parallel operation
set is used to check if there are uncommon characters, if so len will be > 1

'''


class Solution:
    def longestCommonPrefix(self, strs):
        prefix=[]
        num = len(strs)
        # zip(*iterables) unpacks list, tuples, dicts in parallel
        for x in zip(*strs):
            ''' 
            x will look like below
            ('f', 'f', 'f')
            ('l', 'l', 'l')
            ('o', 'o', 'i')
            '''
            if len(set(x))==1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)
        
        
obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
