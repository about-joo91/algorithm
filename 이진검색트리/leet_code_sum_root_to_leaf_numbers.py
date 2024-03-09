class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def add_root_to_leaf(cur_num: int, cur_node: Optional[TreeNode]) -> None:
            nonlocal result
            if not cur_node.left and not cur_node.right:
                result += (cur_num * 10) + cur_node.val
                return
            
            next_num = (cur_num * 10) + cur_node.val
            if cur_node.left: add_root_to_leaf(next_num, cur_node.left)
            if cur_node.right: add_root_to_leaf(next_num, cur_node.right)
        
        add_root_to_leaf(0, root)
        return result
