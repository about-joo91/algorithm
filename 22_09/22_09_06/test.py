front = ['[','{','(']
back = [']','}',')']
def is_right(s):
    stack = []
    for bracket in s:
        if bracket in front:
            stack.append(bracket)
        elif bracket in back:
            if not stack or stack[-1] != front[back.index(bracket)]:
                return False
            stack.pop()
    if stack:
        return False
    return True

def find_bracket(s):
    bracket = ''
    for i in range(len(front)):
        if s.count(front[i]) != s.count(back[i]):
            bracket = front[i] if s.count(front[i]) < s.count(back[i]) else back[i]
            break
    return bracket

def solution(s):
    N = len(s)
    cnt = 0
    bracket = find_bracket(s)
    
    find_bracket(s)
    
    s = list(s)
    for i in range(N+1):
        s.insert(i, bracket)
        if is_right(''.join(s)):
            cnt+=1
        s.pop(i)

    return cnt


print(solution("(()()()"))