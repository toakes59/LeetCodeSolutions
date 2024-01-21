class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_col_tups = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    row_col_tups +=[(i, element), (element, j), (i // 3, j // 3, element)]
        return len(row_col_tups) == len(set(row_col_tups))