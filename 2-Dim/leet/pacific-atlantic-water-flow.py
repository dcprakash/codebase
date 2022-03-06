'''
https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/
water flow from pacific to atlantic
find coordinates in matrix from which water can flow to both ocean
dfs 
'''


class Solution:
    def isValidCell(r,c,matrix):
        if(r>=0 and r<len(matrix) and c>=0 and c<len(matrix[0])):
            return True
        else:
            return False
    
    
    def printMat(matrix):
        print("[",end="")
        for r in range(0,len(matrix),1):
            print("[",end="")
            for c in range(0,len(matrix[0]),1):
                if(c!=len(matrix[0])-1):
                    print("{},".format(matrix[r][c]),end="")
                else:
                    print("{}".format(matrix[r][c]),end="")
            
            if(r==len(matrix)-1):
                print("]]")
            else:
                print("]")
    
    
    def DFS(matrix, r, c, prev_val,ocean):
        #If not a valid cell
        if(Solution.isValidCell(r,c,matrix)==False):
            return
        else:
            curr_val = matrix[r][c]
            #print("Current pos:{}".format(str((r,c))))
            
            #Our prev_val must be lower because we want to go from low to high (from the "coasts" up to higher elevation cells)
            if(prev_val>curr_val):
                #print("Exited because prev_val:{}>curr_val:{}".format(prev_val,curr_val))
                return
            elif(ocean[r][c]!=0):
                #print("Exited because already visited:{}".format((r,c)))
                return
            else:
                ocean[r][c] = 1
                
                Solution.DFS(matrix,r,c+1,curr_val,ocean) #right
                Solution.DFS(matrix,r,c-1,curr_val,ocean) #left
                Solution.DFS(matrix,r+1,c,curr_val,ocean) #down
                Solution.DFS(matrix,r-1,c,curr_val,ocean) #up


    def pacificAtlantic(self, matrix):
        pacific = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        atlantic = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        
        #Edge case
        if(len(matrix)==0):
            return []
        
        """
        Solution:
        1) We want to navigate from lower to higher vals (reverse flow think of it from going from the coast to the mountain where the water would come from)
        2) We use a 'pacific', 'atlantic' matrixes to keep track of the values we reached from the "coasts"
        3) We use loops to plant 'seeds' at the "coasts" for pacific and atlantic (representing where the water would 'start' from) and then we can think of it as a root 
        growing,any cell we visited we set its val in its respective ocean matrix (atlantic or pacific) to 1 representing we were able to reach it from the coasts
        4) At the end once both the pacific and atlantic matrices are filled, we do a double-for loop to find where we find matching 1s representing cells that were visited
        by both the pacific and atlantic water flows
        """
        
        #Start with pacific 'seeds'
        for c in range(0,len(matrix[0]),1):
            Solution.DFS(matrix,0,c,-1*float('inf'),pacific)
        for r in range(0,len(matrix),1):
            Solution.DFS(matrix,r,0,-1*float('inf'),pacific)
        
        #Start with atlantic 'seeds'
        for c in range(0,len(matrix[0]),1):
            Solution.DFS(matrix,len(matrix)-1,c,-1*float('inf'),atlantic)
        for r in range(0,len(matrix),1):
            Solution.DFS(matrix,r,len(matrix[0])-1,-1*float('inf'),atlantic)
        
        
        Solution.printMat(pacific)
        print("---------")
        Solution.printMat(atlantic)
        listOfCoords = []
        
        for r in range(0,len(matrix),1):
            for c in range(0,len(matrix[0]),1):
                if(atlantic[r][c]==1 and pacific[r][c]==1):
                    listOfCoords.append((r,c))
 
        return listOfCoords


matrix=[[1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]
        
s=Solution()
print(s.pacificAtlantic(matrix))


'''
traverse from matrix edges towards inwards
if matrix[edge] number is smaller than matrix[inwards] number
    water can flow to ocean, so mark that block as 1
after complete marking 1s for all the blocks from where water can flow downwards
compare both pacific and altantic matrix, if they both have 1
    water from that point can flow to both pacific and atlantic ocean

pacific
[[1,1,1,1,1]
[1,1,1,1,1]
[1,1,1,0,0]
[1,1,0,0,0]
[1,0,0,0,0]]
---------

atlantic
[[0,0,0,0,1]
[0,0,0,1,1]
[0,0,1,1,1]
[1,1,1,1,1]
[1,1,1,1,1]]

--------
[(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]

'''