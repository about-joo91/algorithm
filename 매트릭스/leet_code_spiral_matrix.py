class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row_s, row_e = 0, len(matrix)-1
        col_s, col_e = 0, len(matrix[0])-1
        
        while row_s <= row_e and col_s <= col_e:
            for cur_col in range(col_s, col_e+1):
                result.append(matrix[row_s][cur_col])
            row_s +=1
            for cur_row in range(row_s, row_e+1):
                result.append(matrix[cur_row][col_e])
            col_e -= 1
            if row_s <= row_e:
                for cur_col in range(col_e, col_s-1, -1):
                    result.append(matrix[row_e][cur_col])
                row_e -=1
            if col_s <= col_e:
                for cur_row in range(row_e, row_s-1, -1):
                    result.append(matrix[cur_row][col_s])
                col_s +=1
        
        return result


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        n, m = len(matrix), len(matrix[0])
        i, j = 0, -1
        direction = 1

        while n * m > 0:
            for _ in range(m):
                j+= direction
                result.append(matrix[i][j])
            n-=1
            for _ in range(n):
                i += direction
                result.append(matrix[i][j])
            m-=1
            direction *= -1
        
        return result
        
