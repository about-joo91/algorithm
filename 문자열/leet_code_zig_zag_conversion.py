class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cur_row = 0
        going_down = True
        answer = [""] * numRows

        for char in s:
            answer[cur_row] += char
            if cur_row == 0:
                going_down = True
            elif cur_row == numRows-1:
                going_down = False
            
            if going_down:
                cur_row +=1
            else:
                cur_row -=1
        
        return "".join(answer)
        
