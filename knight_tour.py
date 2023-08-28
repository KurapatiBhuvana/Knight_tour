board = [[]]

#Main Function
def knight_board(m, n):
    board = [[0 for i in range(n)] for j in range(m)]
    knight_move(0, 0, board, 0, m, n)
    if count_squares(board) == 0:
        return "For this board it is not possible to visit all squares"

    print_board(board, n)
    return f"The number of squares visited = {(count_squares(board)}"
    
#function to print the final board
def print_board(board, n):
    for i in range(n):
        print("_______", end = "")
        if i == n - 1:
            print("_", end = "\n") 
            
    for h in board:
        for k in h:
            if k < 10:
                print("|___", end = "")
            else:
                print("|__", end = "")
            print (k, end = "__")
        print ("|", end = "\n")

# function to check whether knight positions are within the board
def issafe_board(x, y, m, n):
    return x >= 0 and x < n and y >= 0 and y < m

#function to ensure that the knight visits the square only once
def check_revisit(x, y, board):
    return board[x][y] == 0 

#function to create the possibilities for knight's move
def knight_move(x, y, board, counter, m, n):
    if counter == m * n:
        return True
    if issafe_board(x, y, m, n) == False or check_revisit(x, y, board) == False:
        return False
    board[x][y] = counter + 1
    for x_move, y_move in zip([1, -1, 1, -1, 2, -2, 2, -2], [-2, 2, 2, -2, 1, 1, -1, -1]):
        if knight_move(x + x_move, y + y_move, board, counter + 1, m, n):
            return "The knight visited all the squares"
    board[x][y] = 0
    return False

#function to count no. of squares visited by the knight
def count_squares(board):
    count = 0
    for i in board:
        for j in i:
            if j != 0:
                count += 1
    return count

print(knight_board(6, 6))
print(knight_board(8, 3))
print(knight_board(2, 6))









    
