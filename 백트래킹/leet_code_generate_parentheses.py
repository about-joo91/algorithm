class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(cur: str, open_count: int, close_count: int) -> None:
            if len(cur) == n*2:
                result.append(cur)
                return
            
            if open_count < n:
                backtracking(cur+'(', open_count+1, close_count)
            
            if open_count > close_count:
                backtracking(cur+')', open_count, close_count+1)
        
        result = []
        backtracking('', 0, 0)
        return result
