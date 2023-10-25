class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(str, open, closed):
            if len(str) == 2 * n:
                outputList.append(str)
                return

            if open < n:
                backtrack(str + '(', open + 1, closed)
            if closed < open:
                backtrack(str + ')', open, closed + 1)

        outputList = []
        backtrack('', 0, 0)
        return outputList

