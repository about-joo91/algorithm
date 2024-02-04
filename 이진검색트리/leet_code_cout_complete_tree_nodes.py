class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        stack = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            result += 1
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result

  
