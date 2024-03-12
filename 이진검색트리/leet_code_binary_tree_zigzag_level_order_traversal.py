class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        even_depth = False

        while queue:
            n = len(queue)
            same_depth_nodes = []
            for _ in range(n):
                cur_node = queue.popleft()
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
                same_depth_nodes.append(cur_node.val)
            result.append(same_depth_nodes[::-1] if even_depth else same_depth_nodes)
            even_depth = not even_depth
            
        return result
