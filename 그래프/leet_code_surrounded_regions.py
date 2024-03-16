class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if board[i][j] == 'O':
                        board[i][j] = "N"
                        queue.append((i, j))

        while queue:
            cur_row, cur_col = queue.popleft()

            for d_row, d_col in directions:
                next_row = cur_row + d_row
                next_col = cur_col + d_col

                if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
                    continue
                if board[next_row][next_col] == "O":
                    board[next_row][next_col] = "N"
                    queue.append((next_row, next_col))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"

        return board
