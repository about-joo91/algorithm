class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        result = []
        queue = deque()
        queue.append((root, 0))
        depth = 0
        while queue:
            same_depth_nodes = []
            while queue and queue[0][1] == depth: 
                cur_node, cur_depth = queue.popleft()
                same_depth_nodes.append(cur_node.val)
                if cur_node.left: queue.append((cur_node.left, cur_depth+1))
                if cur_node.right: queue.append((cur_node.right, cur_depth+1))
            depth +=1
            result.append(same_depth_nodes)
        
        return result
