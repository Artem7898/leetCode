"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # Dictionary to store numbers and their indices
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        
        return []  # No solution found

# Example usage
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output should be [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output should be [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output should be [0, 1]
