import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N = int(input().rstrip())
dices = [list(map(int, input().rstrip().split())) for _ in range(N)]
oppsite = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}
answer = 0

def back_tracking(depth, cur_top, cur_sum):
    global answer
    if depth == N:
        answer = max(answer, cur_sum)
        return
    
    dice = dices[depth]
    bottom_idx = dice.index(cur_top)
    ceil_idx = oppsite[bottom_idx]
    max_number = 0
    for i in range(6):
        if i == ceil_idx or i == bottom_idx: continue
        max_number = max(max_number, dice[i])
    back_tracking(depth+1, dice[ceil_idx], cur_sum + max_number)


for i in range(1, 7):
    back_tracking(0, i, 0)

print(answer)