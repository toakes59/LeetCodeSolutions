# Combination_Sum_II
def combinationSum2(candidates, target):
    def backtrack(start, target, current_combo):
        # If the target becomes 0, add the current combination to the result
        if target == 0:
            result.append(current_combo[:])
            return
        # Iterate over candidates, starting from the current index
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # If the current candidate is greater than the remaining target, skip it
            if candidates[i] > target:
                continue
            # Include the current candidate in the combination
            current_combo.append(candidates[i])
            # Recursively explore combinations with the current candidate
            backtrack(i + 1, target - candidates[i], current_combo)
            # Backtrack by removing the last added candidate for the next iteration
            current_combo.pop()

    result = []
    candidates.sort()  # Sort the candidates to handle duplicates properly
    backtrack(0, target, [])
    return result

# Example usage:
candidates = [10,1,2,7,6,1,5]
target = 8
result = combinationSum2(candidates, target)
print(result)  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
