from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        extend_list = []
        this_list = [extend_list.append(i) for i in nums]
        return nums + extend_list

solution = Solution()
print(solution.getConcatenation([1, 2, 1]))