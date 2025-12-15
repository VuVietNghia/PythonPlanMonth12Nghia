from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))
print(solution.reverseString(["H", "a", "n", "n", "a", "h"]))
