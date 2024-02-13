class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        result = 0
        left = 0
        for i in range(1, len(s)):
            while s[i] in s[left:i]:
                left +=1
            result = max(result, i - left+1)
        
        return result
        
