class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        i = 0
        result = 0
        while i < n:
            if i < n - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result += roman_dict[s[i + 1]] - roman_dict[s[i]]
                i += 2
            else:
                result += roman_dict[s[i]]
                i += 1
        return result

solution = Solution()
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
print(solution.romanToInt("III"))