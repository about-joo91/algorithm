class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        while zeros:
            cur_row, cur_col = zeros.pop()

            for row in range(len(matrix)):
                matrix[row][cur_col] = 0
            for col in range(len(matrix[0])):
                matrix[cur_row][col] = 0
        
        
