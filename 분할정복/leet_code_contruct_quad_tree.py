class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.make_quad_tree(grid, 0, 0, len(grid))
    
    def make_quad_tree(self, grid: List[List[int]], row: int, col: int, dist: int):
        if self.is_all_same(grid, row, col, dist):
            return Node(grid[row][col], True)
        
        node = Node(grid[row][col], False)
        next_dist = dist//2
        node.topLeft = self.make_quad_tree(grid, row, col, next_dist)
        node.topRight = self.make_quad_tree(grid, row, col+next_dist, next_dist)
        node.bottomLeft = self.make_quad_tree(grid, row+next_dist, col, next_dist)
        node.bottomRight = self.make_quad_tree(grid, row+next_dist, col+next_dist, next_dist)

        return node

    def is_all_same(self, grid: List[List[int]], row: int, col: int, dist: int):
        for i in range(row, row + dist):
            for j in range(col, col + dist):
                if grid[i][j] != grid[row][col]:
                    return False
        return True
