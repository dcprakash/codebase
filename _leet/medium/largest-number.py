'''
magic methods: https://portingguide.readthedocs.io/en/latest/comparisons.html
https://leetcode.com/problems/largest-number/
biggest number
largest number
big number
'''

class LargerNumKey(str):
    def __lt__(x, y):
    	# print(x+y > y+x)	# False
    	# print(x+y , y+x)	# ('303', '330')
        return x+y > y+x

        
class Solution:
    def largestNumber(self, nums):
    	# print(map(str,nums))	# ['3', '30', '34', '9', '5']
    	# print(sorted(map(str,nums)))	# ['3', '30', '34', '5', '9']
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # return largest_num	# if all are 0, this return does not work
        return '0' if largest_num[0] == '0' else largest_num


nums = [3,30,34,9,5]       
s=Solution()
print(s.largestNumber(nums))