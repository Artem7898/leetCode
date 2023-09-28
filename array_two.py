"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchRange(self, nums, target):
        left = self.find_leftmost(nums, target)
        right = self.find_rightmost(nums, target)
        return [left, right]

    def find_leftmost(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left < len(nums) and nums[left] == target:
            return left
        return -1

    def find_rightmost(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0 and nums[right] == target:
            return right
        return -1

# Example 1
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
solution = Solution()
print(solution.searchRange(nums1, target1))  # Output should be [3, 4]

# Example 2
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(solution.searchRange(nums2, target2))  # Output should be [-1, -1]

# Example 3
nums3 = []
target3 = 0
print(solution.searchRange(nums3, target3))  # Output should be [-1, -1]


