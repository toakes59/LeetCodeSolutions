# N-Queens
def solveNQueens(n):
    # Define a function 'is_safe' that checks if placing a queen at a given position (row, col)
    # is safe, considering the queens placed in previous rows.
    def is_safe(board, row, col):
        # Iterate through each previous row (up to 'row' - 1) to check for conflicts.
        for i in range(row):
            # Check if there is a queen in the same column or along the diagonals.
            if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
                # There is a conflict, so placing a queen at this position is not safe.
                return False
        # No conflict found, placing a queen at this position is safe.
        return True

    # Define a function 'solve' that recursively solves the N-Queens problem.
    def solve(row):
        # Base case: If all queens are placed successfully (up to the last row), add the solution.
        if row == n:
            solutions.append([''.join(['Q' if j == col else '.' for j in range(n)]) for col in board])
            return
        # Try placing a queen in each column of the current row.
        for col in range(n):
            # Check if placing a queen at this position is safe.
            if is_safe(board, row, col):
                # If safe, update the 'board' and move on to the next row.
                board[row] = col
                solve(row + 1)

    # Initialize an empty list 'solutions' to store the final solutions.
    solutions = []

    # Initialize the 'board' as a list of length 'n' with all elements set to -1.
    board = [-1] * n

    # Start solving the N-Queens problem with the initial row set to 0.
    solve(0)

    # Return the list of solutions.
    return solutions


# Example usage:
n = 4
result = solveNQueens(n)
print(result)
