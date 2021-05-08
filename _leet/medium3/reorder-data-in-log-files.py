'''
https://leetcode.com/problems/reorder-data-in-log-files/

['dig1', '8', '1', '5', '1']
check if 1st index is alphabetical or digit, since 8 is not alphabetical, we add to digit list



txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x) will print ['apple', 'banana#cherry#orange']
txt.split("#", 2) will print ['apple', 'banana', 'cherry#orange']

x=['let2', 'own', 'kit', 'dig']
x.split(' ', 1)[1]  -> 'own', 'kit', 'dig'

sort
similar to top-k-frequent-words

'''

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isalpha():    # check if 1st index is char or digit (not 0th index)
                letter.append(log)
            else:
                digit.append(log)
        
        # setting the maxsplit parameter to 1, will return a list with 2 elements
        # x is used at the end, is to do another iteration of sort based on let1, let2
        letter.sort(key=lambda x: (x.split(' ', 1)[1], x))
        return letter + digit

s=Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))