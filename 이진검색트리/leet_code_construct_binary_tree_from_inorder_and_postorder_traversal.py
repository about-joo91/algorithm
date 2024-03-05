class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            last_node = postorder.pop()
            idx = inorder.index(last_node)
            root = TreeNode(last_node)

            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            
            return root
