class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sorted_str = ''.join(sorted(word))

            if sorted_str not in result: result[sorted_str] = [word]
            else: result[sorted_str].append(word)

        return result.values()
        
