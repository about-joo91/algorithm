class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def doValidate(cur_node, left, right):
            if not cur_node:
                return True
            
            if cur_node.val <= left or cur_node.val >= right:
                return False
            
            return doValidate(cur_node.left, left, cur_node.val) and doValidate(cur_node.right, cur_node.val, right)
        
        return doValidate(root, float('-inf'), float('inf'))
