# Trapping_Rain_Water
def trap(height):
    # Check if the input height array is empty
    if not height:
        return 0  # If empty, no water can be trapped
    
    n = len(height)
    
    # Initialize arrays to store the maximum height to the left and right of each position
    left_max = [0] * n
    right_max = [0] * n
    
    # Initialize the left_max array by filling it with the maximum height to the left of each position
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Initialize the right_max array by filling it with the maximum height to the right of each position
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Initialize a variable to store the total trapped water
    water_trapped = 0
    
    # Iterate through each position and calculate the trapped water at that position
    for i in range(n):
        # The trapped water at a position is the minimum of the maximum heights to the left and right, minus the height at that position
        water_trapped += min(left_max[i], right_max[i]) - height[i]

    # Return the total trapped water
    return water_trapped


# Example usage:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trap(height)
print(result)  # Output: 6
