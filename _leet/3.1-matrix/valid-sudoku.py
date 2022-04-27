'''
https://leetcode.com/problems/valid-sudoku/
https://www.youtube.com/watch?v=64xGbZthv6Y&feature=emb_logo&ab_channel=LeetDev
'''


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]   # [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        columns = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    # instead of doing for j in range and for i in range for col
                        # if take current iteration and store in dict; 
                        # as iterating col order does not matter, as long as we look for duplicate
                    columns[j][num] = columns[j].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1:
                        return False   
        
        def validGrid(row, col):
            boxes = [{}]
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j]!='.':
                        num=int(board[i][j])
                        boxes[0][num]=boxes[0].get(num,0)+1
                        if boxes[0][num]>1: return False
            
            return True
            
        
        for i in range(3):
            for j in range(3):
                # get starting point of sub martix
                if (not validGrid(i*3, j*3)):  
                    return False
        
        return True
        
sol=Solution()
# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]
        
board = [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]
print(sol.isValidSudoku(board))