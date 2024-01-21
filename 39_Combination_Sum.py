# Combination_Sum
def combinationSum(candidates, target):
    def backtrack(start, target, current_combo):
        # If the target becomes 0, add the current combination to the result
        if target == 0:
            result.append(current_combo[:])
            return
        # Iterate over candidates, starting from the current index
        for i in range(start, len(candidates)):
            # If the current candidate is greater than the remaining target, skip it
            if candidates[i] > target:
                continue
            # Include the current candidate in the combination
            current_combo.append(candidates[i])
            # Recursively explore combinations with the current candidate
            backtrack(i, target - candidates[i], current_combo)
            # Backtrack by removing the last added candidate for the next iteration
            current_combo.pop()

    result = []
    candidates.sort()  # Sort the candidates to handle duplicates properly
    backtrack(0, target, [])
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)  # Output: [[2, 2, 3], [7]]


0, 7, []
0, 5, [2]
0, 3, [2, 2]
0, 1, [2, 2, 2]
1, 3, [2, 2]
1, 0, [2, 2, 3] -> add to Output
