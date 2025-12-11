class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        for char in ransom_note:
            if char in magazine:
                magazine = magazine.replace(char, '', 1)
            else:
                return False
        return True

solution = Solution()
print(solution.canConstruct("aa", "ab"))