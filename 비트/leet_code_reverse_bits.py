class Solution:
    def reverseBits(self, n: int) -> int:
        result = ''
        for i in range(32):
            n, mod = divmod(n, 2)
            result += str(mod)
        
        return int(result, 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            result = result << 1 | (n & 1)
            n >>= 1
        
        return result
