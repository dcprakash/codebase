'''
https://leetcode.com/problems/palindrome-partitioning/solution/

# palindrome partition backtracking
Iteratively generate all possible substrings beginning at start index. The end index increments from start till the end of the string.
    Example, abba can be partitioned as ["a","ab","abb","abba"]
For each of the substring generated, check if it is a palindrome.
If the substring is a palindrome, the substring is a potential candidate. Add substring to the \text{currentList}currentList and perform a depth-first search on the remaining substring. 
Backtrack if \text{start}start index is greater than or equal to the string length and add the \text{currentList}currentList to the result.

'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(lo,hi):
            while lo<=hi:
                if s[lo]!=s[hi]:    return False
                lo+=1
                hi-=1
            return True
        
        
        def dfs(start_ind, path):
            n=len(s)
            if start_ind >= n:
                # print(path)   # currentList
                self.res.append(path)
                
            for l in range(n - start_ind): #0,3; 0,2; 0,1
                if isPalindrome(start_ind, start_ind + l):
                    dfs(start_ind + l + 1, path + [s[start_ind : start_ind + l + 1]] )
                    # dfs(0, []), dfs(1, [a]), dfs(2,[a,a]), dfs(3,[a,a,b])
        
        self.res = []
        dfs(0,[])
        return self.res

s=Solution()
print(s.partition("aab"))
