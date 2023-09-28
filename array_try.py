"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""


class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        curr_reach = 0
        max_reach = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_reach:
                jumps += 1
                curr_reach = max_reach

        return jumps

# Example usage
nums = [2, 3, 0, 1, 4]
solution = Solution()
print(solution.jump(nums))  # Output should be 2

