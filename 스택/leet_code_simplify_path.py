class Solution:
    def simplifyPath(self, path: str) -> str:        
        stack = []
        paths = list(filter(lambda x: x, path.split('/')))
        for el in paths:
            if el == '..':
                if stack:
                    stack.pop()
            elif el == '.':
                continue
            else:
                stack.append(el)

        return '/' + '/'.join(stack)
