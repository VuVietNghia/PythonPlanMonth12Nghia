from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        print(nums)

solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])