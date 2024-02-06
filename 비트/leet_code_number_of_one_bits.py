class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n, mod = divmod(n, 2)
            if mod == 1:
                count+=1
        
        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count +=1
            n &= (n-1)
        
        return count
