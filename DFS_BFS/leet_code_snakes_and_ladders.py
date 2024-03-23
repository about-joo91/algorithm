class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def to_coordinates(square:int, n: int) -> Tuple[int, int]:
            div, mod = divmod(square-1, n)
            row = n - 1 - div
            col = mod if row % 2 != n % 2 else n - 1 - mod
            return row, col

        n = len(board)
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, move_count = queue.popleft()
            if square == n*n:
                return move_count
            
            for n_square in range(square+1, min(square+7, n*n+1)):
                row, col = to_coordinates(n_square, n)
                if board[row][col] != -1:
                    n_square = board[row][col]
                if n_square not in visited:
                    queue.append((n_square, move_count+1))
                    visited.add(n_square)
        
        return -1
