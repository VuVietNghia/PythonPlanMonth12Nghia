from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = len(height)
        left, right = 0, s - 1
        max_length = 0

        while left < right and right < s:
            area = (right - left) * min(height[left], height[right])

            if area > max_length:
                max_length = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_length

solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# 8 7 2 1
# |     | 3
# |    |  2 * 2 = 4
# |  |    1 * 7 = 7

# (j - i) * min(height[i], height[j])
#   1 6 2 2 4 4 3 3 - in between each line
# 1 8 6 2 5 4 8 3 7
# |               |
# (8 - 0) * 1 = 8 => take min and shift to one; max = 8
#   |             |
# (8 - 1) * 7 = 49 => take min and shift to one; max = 49
#   |            |
# (7 - 1) * 3 = 21 => take min and shift to one; max = 49
#   |         |
# (6 - 1) * 8 = 40 => take min and shift to one; max = 49
# ....