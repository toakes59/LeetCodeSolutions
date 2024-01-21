class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def solve(row):
            if row == n:
                solutions.append([''.join(['Q' if j == col else '.' for j in range(n)]) for col in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1)

        solutions = []
        board = [-1] * n
        solve(0)
        return solutions