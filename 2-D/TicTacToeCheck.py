# Python3 program to check whether a given tic tac toe
# board is valid or not
# https://www.geeksforgeeks.org/validity-of-a-given-tic-tac-toe-board-configuration/
# Returns true if char wins. Char can be either
# 'X' or 'O'
def win_check(arr, char):
    # Check all possible winning combinations
    # first, second and third row
    # first, second and third column
    # 2 diagnoals
    matches = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

    for i in range(8):
        # print(matches[i])
        print(matches[i][0])
        print(matches[i][1])
        print(matches[i][2])
        # print(arr[matches[i][0]])
        # print(arr[matches[i][0]] + arr[matches[i][1]] + arr[matches[i][2]])
        print("............")
        if (arr[matches[i][0]] == char and
                arr[matches[i][1]] == char and
                arr[matches[i][2]] == char):
            return True
    return False


def is_valid(arr):
    # Count number of 'X' and 'O' in the given board
    xcount = arr.count('X')
    ocount = arr.count('O')

    # Board can be valid only if either xcount and ocount
    # is same or xount is one more than oCount
    if (xcount == ocount + 1 or xcount == ocount):
        # Check if O wins
        if win_check(arr, 'O'):
            # Check if X wins, At a given point only one can win,
            # if X also wins then return Invalid
            if win_check(arr, 'X'):
                return "Invalid"

            # O can only win if xcount == ocount in case where whole
            # board has values in each position.
            if xcount == ocount:
                return "Valid"

        # If X wins then it should be xc == oc + 1,
        # If not return Invalid
        if win_check(arr, 'X') and xcount != ocount + 1:
            return "Invalid"

        # if O is not the winner return Valid
        if not win_check(arr, 'O'):
            return "Valid"

    # If nothing above matches return invalid
    return "Invalid"


# Driver Code
arr = ['X', 'X', 'O',
       'O', 'O', 'X',
       'X', 'O', 'X']
print("Given board is " + is_valid(arr))
