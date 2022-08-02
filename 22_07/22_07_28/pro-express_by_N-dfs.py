def dfs(N, num_now, answer_num,depth, answer):
    if depth > 8:
        return
    if num_now == answer_num:
        answer.append(depth)
        return
    next_N = 0
    for i in range(9):
        next_depth = depth + i +1
        next_N = (next_N *10) + N
        dfs(N, num_now + next_N ,answer_num, next_depth , answer)
        dfs(N, num_now - next_N , answer_num,next_depth , answer)
        dfs(N, num_now * next_N ,answer_num, next_depth , answer)
        dfs(N, num_now // next_N , answer_num,next_depth, answer)   
    
def solution(N, number):
    answer = []
    dfs(N, 0,number, 0,  answer)
    
    if len(answer) < 1:
        return -1
    return min(answer)

print(solution(5, 12))