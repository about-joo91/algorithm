class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        
        while left <= right:
            if not s[left].isalnum():
                left +=1
            elif not s[right].isalnum():
                right -=1
            else:
                if s[left] != s[right]:
                    return False
            
                left +=1
                right -=1
        
        return True


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(s)-1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
