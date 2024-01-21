# First_Missing_Positive
def firstMissingPositive(nums):
    n = len(nums)
    
    # Rearrange the array so that nums[i] = i + 1 for each valid i
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first index i such that nums[i] != i + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all numbers are in their correct place, the first missing positive is n + 1
    return n + 1

# Example usage:
nums = [3, 4, -1, 1]
result = firstMissingPositive(nums)
print(result)  # Output: 2
