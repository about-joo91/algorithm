from typing import List


class Solution:
    DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.checkNewIsland(i, j, grid)
                    count += 1

        return count

    def checkNewIsland(self, row: int, col: int, grid: List[List[str]]):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "0":
            return

        grid[row][col] = "0"
        for d_row, d_col in self.DIRECTIONS:
            next_row = row + d_row
            next_col = col + d_col

            self.checkNewIsland(next_row, next_col, grid)
