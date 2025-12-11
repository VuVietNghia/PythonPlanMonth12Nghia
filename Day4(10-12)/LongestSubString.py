class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        hash_set = set()

        while right < len(s):
            if s[right] not in hash_set:
                hash_set.add(s[right])
                right += 1
                max_length = max(max_length, len(hash_set))
            else:
                hash_set.remove(s[left])
                left += 1
        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring("abcdzdcba"))