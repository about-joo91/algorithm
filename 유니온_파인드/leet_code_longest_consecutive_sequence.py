class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class UnionFind:
    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            root_y.parent = root_x
            root_x.size += root_y.size
        return root_x.size

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = uf.union(node, nodes[num+1])
                if num - 1 in nodes:
                    size = uf.union(node, nodes[num-1])
                max_size = max(max_size, size)
                
        return max_size
