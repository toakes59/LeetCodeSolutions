# Sudoku_Solver
def solveSudoku(board):
    def is_valid(num, row, col):
        # Check if the number is not present in the current row, column, and sub-grid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve():
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    # Try placing numbers from 1 to 9
                    for num in map(str, range(1, 10)):
                        if is_valid(num, i, j):
                            # If placing the number is valid, update the board and continue solving
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."  # Backtrack if the current placement is not valid
                    return False  # If no valid number can be placed, backtrack to the previous state
        return True  # If all cells are filled, the board is solved

    solve()


# Example usage:
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(sudoku_board)
print(sudoku_board)
