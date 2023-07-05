N, K = map(int, input().split())

answers = []

def make_next_str(cur_str, idx):
    return str(idx) if cur_str == '' else cur_str + '+' + str(idx)

def back_tracking(cur_num, cur_str):
    if cur_num > N: return
    elif cur_num == N:
        answers.append(cur_str)
        return
    
    for i in range(1, 4):
        next_str = make_next_str(cur_str, i)
        back_tracking(cur_num+i, next_str)


back_tracking(0, '')
print(answers[K-1] if len(answers) >= K else -1)