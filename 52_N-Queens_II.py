class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def solve(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1)

        count = 0
        board = [-1] * n
        solve(0)
        return count