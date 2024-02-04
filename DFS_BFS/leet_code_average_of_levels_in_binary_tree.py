class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        same_level_nodes = deque([root])

        while same_level_nodes:
            sum_of_nodes = 0
            count_of_nodes = 0
            for _ in range(len(same_level_nodes)):
                cur = same_level_nodes.popleft()
                sum_of_nodes += cur.val
                count_of_nodes += 1
                if cur.left:
                    same_level_nodes.append(cur.left)
                if cur.right:
                    same_level_nodes.append(cur.right)
            
            result.append(sum_of_nodes / count_of_nodes)
        
        return result
