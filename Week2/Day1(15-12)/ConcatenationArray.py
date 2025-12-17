from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        this_list = [i * 2 for i in nums]
        return nums + this_list

solution = Solution()
print(solution.getConcatenation([1, 2, 1]))