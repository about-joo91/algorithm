class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        def make_order_nodes(node):
            if node is None:
                return

            make_order_nodes(node.left)
            nodes.append(node.val)
            make_order_nodes(node.right)
        
        make_order_nodes(root)
        min_diff = int(10e5)
        for i in range(1, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i-1])
        
        return min_diff
        
