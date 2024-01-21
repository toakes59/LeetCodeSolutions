class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, current_combo):
            if target == 0:
                result.append(current_combo[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    continue

                current_combo.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combo)
                current_combo.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result