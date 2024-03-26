class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def make_combine(current_comb: List[int], next_idx: int) -> None:
            if len(current_comb) == k:
                result.append(current_comb[:])
                return

            for i in range(next_idx, n+1):
                current_comb.append(i)
                make_combine(current_comb, i+1)
                current_comb.pop()
        
        make_combine([], 1)
        return result
