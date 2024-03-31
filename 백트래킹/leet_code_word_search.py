class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_word(depth: int, row: int, col: int, word: str) -> None:
            nonlocal result

            if depth == len(word):
                result = True
                return

            for direction in directions:
                n_row = row+ direction[0]
                n_col = col+ direction[1]
                if n_row < 0 or n_row >= N or n_col < 0 or n_col >= M:
                    continue
                if visited[n_row][n_col]:
                    continue
                if board[n_row][n_col] != word[depth]:
                    continue

                visited[n_row][n_col] = True
                search_word(depth+1,n_row,n_col,word)
                visited[n_row][n_col] = False

        
        N = len(board)
        M = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = False
        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    visited = [[False] * M for _ in range(N)]
                    visited[i][j] = True
                    search_word(1, i, j, word)
        
        return result
