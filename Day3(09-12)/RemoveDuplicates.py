from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        this_list = []
        for i in range(len(nums)):
            if nums[i] not in this_list:
                this_list.append(nums[i])
        return len(this_list)

solution = Solution()
print(solution.removeDuplicates([1, 1, 2, 2, 3]))
