class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                
                while prev.right:
                    prev = prev.right
                
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            
            cur = cur.right

class Solution:
    prev_node = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev_node
        root.left = None
        self.prev_node = root
