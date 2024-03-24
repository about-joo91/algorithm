class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        gene_candidates = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            cur_gene, mut_count = queue.popleft()
            
            if cur_gene == endGene:
                return mut_count

            for i in range(len(cur_gene)):
                for candidate in gene_candidates:
                    next_gene = cur_gene[:i] + candidate + cur_gene[i+1:]
                    if next_gene not in visited and next_gene in bank:
                        queue.append((next_gene, mut_count+1))
                        visited.add(cur_gene)
        
        return -1
