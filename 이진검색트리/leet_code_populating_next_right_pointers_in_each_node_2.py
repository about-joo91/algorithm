class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node_map = defaultdict(list)
        self.set_next_node(root, 0, node_map)

        return root
        
    
    def set_next_node(self, node: 'Node', depth: int, node_map: dict) -> 'Node':
        if node == None:
            return

        self.set_next_node(node.left, depth+1, node_map)
        self.set_next_node(node.right, depth+1, node_map)

        if depth in node_map:
            prev_node = node_map[depth].pop()
            prev_node.next = node
        node_map[depth].append(node)
