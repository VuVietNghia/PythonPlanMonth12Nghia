from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = 0
        min_length = float('inf')

        for right in range(len(nums)):
            result += nums[right]
            while result >= target:
                min_length = min(min_length, right - left + 1)
                result -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(4, [1, 4, 4]))
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))