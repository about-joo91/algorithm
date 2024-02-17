class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for i in range(len(matrix)):
            matrix[i].reverse()

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        l = 0
        r = n - 1

        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l +=1
            r -=1

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
