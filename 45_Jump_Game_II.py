# Jump_Game_II
def jump(nums):
    # Get the length of the input array
    n = len(nums)

    # If there is only one element in the array, no jumps are needed (already at the last index)
    if n == 1:
        return 0

    jumps = 0  # Initialize the number of jumps
    curr_end = 0  # Initialize the current farthest position that can be reached
    farthest = 0  # Initialize the farthest position that can be reached after the current jump

    # Iterate through the array, except for the last element
    for i in range(n - 1):
        # Update the farthest position that can be reached after the current jump
        farthest = max(farthest, i + nums[i])

        # If the current position is equal to the current farthest position that can be reached
        if i == curr_end:
            jumps += 1  # Increment the number of jumps
            curr_end = farthest  # Update the current farthest position

            # If the current farthest position is greater than or equal to the last index, break the loop
            if curr_end >= n - 1:
                break

    return jumps  # Return the total number of jumps needed to reach the last index


# Example usage:
nums = [2, 3, 1, 1, 4]
result = jump(nums)
print(result)  # Output: 2
