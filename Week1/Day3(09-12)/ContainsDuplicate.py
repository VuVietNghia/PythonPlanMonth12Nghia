from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        this_list = []
        for i in nums:
            if i in this_list:
                return True
            this_list.append(i)
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))