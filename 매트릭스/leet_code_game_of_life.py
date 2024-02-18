class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        diffs = []
        directions = [(0,1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1),(0,-1),(-1,0)]
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_cell_count = 0

                for d in directions:
                    nr = row + d[0]
                    nc = col + d[1]
                
                    if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == 1:
                        live_cell_count += 1

                if board[row][col] == 1:
                    if live_cell_count < 2:
                        diffs.append((row, col, 0))
                    elif live_cell_count > 3:
                        diffs.append((row, col, 0))
                else:
                    if live_cell_count == 3:
                        diffs.append((row, col, 1))
            
        for row, col, next_live in diffs:
            board[row][col]= next_live
