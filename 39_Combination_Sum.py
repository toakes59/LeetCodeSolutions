class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, current_combo):
            if target == 0:
                result.append(current_combo[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                current_combo.append(candidates[i])
                backtrack(i, target - candidates[i], current_combo)
                current_combo.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result