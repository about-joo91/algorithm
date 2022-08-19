import sys
iter_num = int(sys.stdin.readline())
LIMIT_LEN = 11
answer = []
def permutation_with_repetition():
    global cnt
    if len(answer) == LIMIT_LEN:
        return
    if sum(answer) == check_num:
        cnt+=1
    for i in range(1, 4):
        answer.append(i)
        permutation_with_repetition()
        answer.pop()
for _ in range(iter_num):
    check_num = int(sys.stdin.readline())
    cnt = 0
    permutation_with_repetition()
    print(cnt)