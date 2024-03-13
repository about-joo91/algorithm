class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_nodes = []
        self.load_ordered_nodes(root, ordered_nodes)

        return ordered_nodes[k-1]

    def load_ordered_nodes(self, cur_node: Optional[TreeNode], ordered_nodes: list):
        if not cur_node:
            return

        self.load_ordered_nodes(cur_node.left, ordered_nodes)
        ordered_nodes.append(cur_node.val)
        self.load_ordered_nodes(cur_node.right, ordered_nodes)
