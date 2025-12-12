from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] != nums[left]:
                left += 1
                nums[left] = nums[i]
        return left + 1

        # this_list = []
        # for i in nums:
        #     if i not in this_list:
        #         this_list.append(i)
        # nums = this_list
        # return len(this_list)


solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
