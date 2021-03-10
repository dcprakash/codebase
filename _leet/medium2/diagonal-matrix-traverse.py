'''
https://leetcode.com/problems/diagonal-traverse/
https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
digonal matric traverse

so 2 key facts:
1. Diagonals are defined by the sum of indicies in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, 
    therefore check if divisible by 2
'''

from collections import defaultdict

class Solution(object):
    def countComponents(self, matrix):
        
        d = defaultdict(list)
        # defaultdict(<class 'list'>, {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]})
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[i+j].append(matrix[i][j])
                
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                # [ans.append(x) for x in entry[1][::-1]]
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        
        return ans


matrix= [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
s=Solution()
print(s.countComponents(matrix))