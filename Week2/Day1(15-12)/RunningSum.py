from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        sum_list = []
        for i in nums:
            s += i
            sum_list.append(s)
        return sum_list

solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))