def checkPalindrome(s: str) -> bool:
    forward_list = []
    backward_list = []
    for i in s:
        forward_list.append(i)
        backward_list.append(i)
    backward_list.reverse()
    return forward_list == backward_list

print(checkPalindrome("racecar"))
