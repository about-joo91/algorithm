class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        weight = 1
        i = len(digits)-1
        while weight:
            if i < 0:
                digits.insert(0, weight)
                break
            cur_num = digits[i] + weight
            weight = cur_num//10
            digits[i] = cur_num % 10
            i-=1

        return digits
