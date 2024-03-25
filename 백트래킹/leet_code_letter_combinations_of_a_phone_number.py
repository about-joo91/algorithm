class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        number_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxzy'
        }

        def backtrack(combination: str, index: int) -> None:
            if index == len(digits):
                result.append(combination)
            else:
                for letter in number_map[digits[index]]:
                    backtrack(combination + letter, index+1)
        result = []
        backtrack("", 0)
        return result
