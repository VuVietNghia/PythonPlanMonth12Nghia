from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for i in nums:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        return even_list + odd_list

solution = Solution()
print(solution.sortArrayByParity([3, 1, 2, 4]))