

'''
https://leetcode.com/problems/candy-crush/solution/

crush:
    mark candies that need to be crushed first
    123
    145
    111
    and we crush the vertical row of 1s early, we may not see there was also a horizontal row.

    mark board's entry with "-<entry>" to show its crushed
        board[i][j] = -Math.abs(board[i][j]))
    if we find contiguous segments of 3 or more in column or row, flag them
    crush the candy, mark them 0

gravity step: all candys should go down
    read and write head; iterate in reverse order through columns
        when read sees candy, write will write it down and move one place
        write 0 to reminder of column
        
repeat candy crush recursively until there is no todo
    
'''

class Solution(object):
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        return self.candyCrush(board) if todo else board
       
board =[
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]]
s=Solution()
print(s.candyCrush(board))

''' 
 [
0    [110,   5,      112,    113,    114], 
1    [210,   211,    5,      213,    214], 
2    [310,   311,    3,      313,     314], 
3    [410,   411,    412,     5,     414], 
4    [5,     1,      512,    3,       3], 
5    [610,   4,      1,      613,     614], 
6    [710,   -1,     -2,     713,     714], 
7    [810,   -1,     -2,     1,       1], 
8    [1,     -1,     -2,     -2,      -2], 
9    [4,     -1,     4,      4,      1014]
 
      0       1       2       3       4
 ]
 
 
 #after second column, will have below
 [
 [110,  0, 112, 113, 114], 
 [210,  0, 5, 213, 214], 
 [310,  0, 3, 313, 314], 
 [410,  0, 412, 5, 414], 
 [5,    5, 512, 3, 3], 
 [610, 211, 1, 613, 614], 
 [710, 311, -2, 713, 714], 
 [810, 411, -2, 1, 1], 
 [1,    1, -2, -2, -2], 
 [4,    4, 4, 4, 1014]
 ]
 
 
 
    9,1     8,1     7,1     6,1     wont decrease wr; so wr=3 instead of -1
    3,1     2,1     1,1     0,1     becomes 0
    which looks like below
     [110,   5,      112,    113,    114], 
1    [210,   0,    5,      213,    214], 
2    [310,   0,    3,      313,     314], 
3    [410,   0,    412,     5,     414], 
4    [5,     0,      512,    3,       3], 
5    [610,   4,      1,      613,     614], 
6    [710,   -1,     -2,     713,     714], 
7    [810,   -1,     -2,     1,       1], 
8    [1,     -1,     -2,     -2,      -2], 
9    [4,     -1,     4,      4,      1014]
 
      0       1       2       3       4
      
      
      
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [110, 0, 0, 0, 114], 
    [210, 0, 0, 0, 214], 
    [310, 0, 0, 113, 314], 
    [410, 0, 0, 213, 414], 
    [610, 211, 112, 313, 614], 
    [710, 311, 412, 613, 714], 
    [810, 411, 512, 713, 1014]]
'''
