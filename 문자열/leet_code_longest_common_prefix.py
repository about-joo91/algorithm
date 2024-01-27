class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''

        strs.sort()
        for char_f, char_l in zip(strs[0], strs[-1]):
            if char_f != char_l:
                break
            answer += char_f

        return answer
