class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def pathSumCalculator(cur_sum, cur_node):
            if cur_node is None:
                return False    
            
            cur_sum += cur_node.val
            if cur_node.left is None and cur_node.right is None:
                return cur_sum == targetSum
            
            return pathSumCalculator(cur_sum, cur_node.left) or pathSumCalculator(cur_sum, cur_node.right)

        return pathSumCalculator(0, root)
