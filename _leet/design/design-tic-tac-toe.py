"""
https://leetcode.com/problems/design-tic-tac-toe/

"""

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n=n
        self.grid=[[0]*n for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.grid[row][col]=player
        if self.check_grid(row, col):
            return player
        return 0
        
    
    def check_grid(self, row, col):
        is_hor, is_vec = True, True
        for i in range(self.n):
            if self.grid[row][i] != self.grid[row][col]:
                is_hor = False
                break
        for i in range(self.n):
            if self.grid[i][col] != self.grid[row][col]:
                is_vec = False
                break
        return is_hor or is_vec or self.check_dia(row, col) or self.check_anti_dia(row, col)


    def check_dia(self, row, col):
        if row != col:
            return False
        for i in range(self.n):
            if self.grid[i][i] != self.grid[row][col]:
                return False
        return True
    
    
    def check_anti_dia(self, row, col):
        if row + col != self.n - 1:
            return False
        for i in range(self.n):
            if self.grid[i][self.n - 1 - i] != self.grid[row][col]:
                return False
        return True
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)