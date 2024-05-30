def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(board, row, num):
    return any(board[row][col] == num for col in range(9))

def used_in_col(board, col, num):
    return any(board[row][col] == num for row in range(9))

def used_in_box(board, row, col, num):
    return any(board[i][j] == num for i in range(row, row + 3) for j in range(col, col + 3))

def check_location_is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row - row % 3, col - col % 3, num)

def solve_sudoku(board):
    l = [0, 0]
    if not find_empty_location(board, l):
        return True
    row, col = l
    for num in range(1, 10):
        if check_location_is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
