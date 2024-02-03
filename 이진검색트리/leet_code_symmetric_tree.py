class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(left, right):
            if not left and not right:
                return True
            elif not left or not right or left.val != right.val:
                return False
            else:
                return check(left.left, right.right) and check(left.right, right.left)
        
        return check(root.left, root.right)
