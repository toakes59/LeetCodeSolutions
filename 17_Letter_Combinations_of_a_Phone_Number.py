class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        backtrack("", digits, map, result)
        return result
    
def backtrack(combination, next_digits, map, result):
    if len(next_digits) == 0:
        result.append(combination)
    else:
        for letter in map[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:], map, result)

