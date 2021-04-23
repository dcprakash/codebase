# https://www.geeksforgeeks.org/a-boolean-matrix-question/
# if matrix[i][j] is 1 then make all cells of ith row and jth column as 1


def booleanMatrix(mat):
    R=len(matrix)
    C=len(matrix[0])
    row = [0] * R # Initialize all values of row[] as 0 
    col = [0] * C 
    
    # Store the rows and columns to be marked  
    # as 1 in row[] and col[] arrays respectively  
    for i in range(0, R) :
        for j in range(0, C) : 
            if (mat[i][j] == 1) : 
                row[i] = 1
                col[j] = 1
    # print(row)  # [0, 1]  all elemends in second row mat will be 1
    # print(col)  # [0, 0, 1]   all elemends in third col mat will be 1
    
    # Modify the input matrix mat[] using the  
    # above constructed row[] and col[] arrays  
    for i in range(0, R) :
        for j in range(0, C): 
            if ( row[i] == 1 or col[j] == 1 ) : 
                mat[i][j] = 1
                
    return mat


# matrix=[[1,0],
#         [0,0]]

matrix=[[0, 0, 0],
        [0, 0, 1]]
        
print(booleanMatrix(matrix))