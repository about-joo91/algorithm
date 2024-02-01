class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.invertTree(root.right)  
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left

        return root
