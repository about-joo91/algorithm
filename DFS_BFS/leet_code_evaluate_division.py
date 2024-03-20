class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, equation in enumerate(equations):
            dividend = equation[0]
            divisor = equation[1]
            graph[dividend].append((divisor, values[idx]))
            graph[divisor].append((dividend, 1 / values[idx]))

            
        result = []
        for query in queries:
            dividend = query[0]
            divisor = query[1]
            if dividend in graph and dividend == divisor:
                result.append(1)
                continue

            queue = deque([(dividend, 1)])
            used = [dividend]
            min_value = float('inf')
            while queue:
                cur_dividend, cur_value = queue.popleft()
                if cur_dividend not in graph: continue
                
                for divisor_cadi, value in graph[cur_dividend]:
                    if divisor_cadi in used: continue
            
                    if divisor_cadi == divisor:
                        min_value = min(min_value, value * cur_value)
                    
                    used.append(divisor_cadi)
                    queue.append((divisor_cadi, value * cur_value))
            
            if min_value == float('inf'):
                result.append(-1)
            else:
                result.append(min_value)
        
        return result
