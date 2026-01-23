class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward_list = []
        backward_list = []
        for i in str(x):
            forward_list.append(i)
        for i in str(x):
            backward_list.append(i)
        backward_list.reverse()
        if forward_list == backward_list:
            return True
        else:
            return False

solution =  Solution()
print(solution.isPalindrome(10))