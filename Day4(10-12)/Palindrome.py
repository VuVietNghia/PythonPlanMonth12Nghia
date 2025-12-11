class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_list = []
        for i in s:
            if i.isalnum():
                forward_list.append(i.lower())
        backward_list = forward_list[::-1]
        return forward_list == backward_list

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))