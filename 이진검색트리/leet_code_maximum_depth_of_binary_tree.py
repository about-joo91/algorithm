class Solution:
    def depthCalculator(self, depth, node):
        if not node:
            return depth
        
        left_depth = self.depthCalculator(depth+1, node.left)
        right_depth = self.depthCalculator(depth+1, node.right)
        return max(left_depth, right_depth)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depthCalculator(0, root)

