class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        depth = 0
        queue = deque()
        queue.append((root, depth))
        while queue:
            while queue and queue[0][1] == depth:
                cur_node, depth = queue.popleft()
                
                if cur_node.left:
                    queue.append((cur_node.left, depth+1))
                if cur_node.right:
                    queue.append((cur_node.right, depth+1))

            result.append(cur_node.val)
            depth+=1
        return result
