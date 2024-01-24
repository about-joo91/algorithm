class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h_index = 0

        for i in range(n):
            h_index = max(h_index, min(citations[i], n - i))
        
        return h_index



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for index, citation in enumerate(citations):
            if index >= citation:
                return index
        return len(citations)
