from collections import deque
def solution(s):
    check_right_parentheses = deque(list(s))
    last_parenth = []
    while check_right_parentheses:
        cur_parenth = check_right_parentheses.popleft()
        if len(last_parenth) == 0 and cur_parenth == ')':
            return False
        elif len(last_parenth) !=0 and cur_parenth != last_parenth[-1]:
            last_parenth.pop()
        else:
            last_parenth.append(cur_parenth)
            
    if len(last_parenth) > 0:
        return False
    return True
