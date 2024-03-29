class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_comb_sum(comb, next_idx):
            if sum(comb) > target:
                return

            if sum(comb) == target:
                result.append(comb[:])
                return

            for idx in range(next_idx, len(candidates)):
                comb.append(candidates[idx])
                find_comb_sum(comb, idx)
                comb.pop()
        
        result = []
        find_comb_sum([], 0)
        return result
