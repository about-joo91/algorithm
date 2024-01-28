class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
