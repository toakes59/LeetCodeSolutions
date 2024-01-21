# Search_in_Rotated_Sorted_Array
def search(nums, target):
    # Initialize left and right pointers for binary search
    left, right = 0, len(nums) - 1

    # Perform binary search while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # Check if the target is in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Adjust the right pointer
            else:
                left = mid + 1  # Adjust the left pointer
        else:  # If the right half is sorted
            # Check if the target is in the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Adjust the left pointer
            else:
                right = mid - 1  # Adjust the right pointer

    # If the target is not found, return -1
    return -1



