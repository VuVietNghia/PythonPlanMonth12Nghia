class Solution:
    def validPalindrome(self, s: str) -> bool:
        forward_list = list(s)
        backward_list = list(s)
        backward_list.reverse()

        for i in forward_list:
            for j in backward_list:
                if forward_list != backward_list:
                    forward_list.remove(i)
                    backward_list.remove(j)
                    return True
                else:
                    return False
            return True

solution = Solution()
print(solution.validPalindrome("aba"))
print(solution.validPalindrome("abca"))
print(solution.validPalindrome("abc"))
print(solution.validPalindrome("deeee"))