class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        while s:
            last_word = s.pop()
            if len(last_word) > 0:
                return len(last_word)
