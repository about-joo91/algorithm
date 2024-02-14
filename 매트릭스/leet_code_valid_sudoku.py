class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        matrix = defaultdict(list)
        for i in range(9):
            for j in range(9):
                matrix_idx = int(str(i//3) + str(j//3), 3)
                cur_num = board[i][j]
                if cur_num == '.':
                    continue
                if cur_num in row[i] or cur_num in col[j] or cur_num in matrix[matrix_idx]:
                    return False

                row[i].append(cur_num)
                col[j].append(cur_num)
                matrix[matrix_idx].append(cur_num)
        
        return True
