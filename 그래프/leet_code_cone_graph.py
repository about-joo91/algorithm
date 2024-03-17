from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        node_queue = deque([node])
        clone_nodes = {node.val: Node(node.val, [])}

        while node_queue:
            cur_node = node_queue.popleft()
            cur_clone = clone_nodes[cur_node.val]

            for adj_node in cur_node.neighbors:
                if adj_node.val not in clone_nodes:
                    clone_nodes[adj_node.val] = Node(adj_node.val, [])
                    node_queue.append(adj_node)
                
                cur_clone.neighbors.append(clone_nodes[adj_node.val])
        
        return clone_nodes[node.val]
