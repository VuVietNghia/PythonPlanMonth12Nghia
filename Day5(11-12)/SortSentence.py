class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = [None] * len(words)
        for word in words:
            index = int(word[-1]) - 1
            sorted_words[index] = word[:-1]
        return ' '.join(sorted_words)

solution = Solution()
print(solution.sortSentence("is2 sentence4 This1 a3"))