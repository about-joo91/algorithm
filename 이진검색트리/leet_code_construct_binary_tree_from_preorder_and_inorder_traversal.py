class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) <= 0:
            return
            
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])

        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])

        return root
