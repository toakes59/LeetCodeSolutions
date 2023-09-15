class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)-2):
            left_point = i + 1
            right_point = len(nums) - 1

            while left_point < right_point:
                total = nums[i] + nums[left_point] + nums[right_point]

                if total == target:
                    return total

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    left_point += 1
                else:
                    right_point -= 1

        return closest_sum

