# Permutationsfrom typing import List
# Define a function named 'permute' that takes a list of integers 'nums' as input
# and returns a list of lists of integers.
def permute(nums: List[int]) -> List[List[int]]:
    # Define a nested function 'backtrack' that takes a parameter 'start'.
    def backtrack(start):
        # Base case: if 'start' is equal to the length of 'nums',
        # it means we have formed a complete permutation.
        if start == len(nums):
            # Append a copy of 'nums' to the 'result' list.
            # (Use 'copy' to avoid modifying the original list later.)
            result.append(nums.copy())
            return
        
        # Iterate through the indices starting from 'start' to the end of 'nums'.
        for i in range(start, len(nums)):
            # Swap the elements at indices 'start' and 'i'.
            nums[start], nums[i] = nums[i], nums[start]
            
            # Recursively call 'backtrack' with the updated 'start'.
            # This explores all possible permutations by swapping elements.
            backtrack(start + 1)
            
            # Undo the swap to backtrack and explore other possibilities.
            nums[start], nums[i] = nums[i], nums[start]

    # Initialize an empty list 'result' to store the permutations.
    result = []
    
    # Start the backtracking process with the initial index set to 0.
    backtrack(0)
    
    # Return the list of all permutations.
    return result


# Example usage:
nums = [1, 2, 3]
result = permute(nums)
print(result)
