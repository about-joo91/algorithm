import sys
input = sys.stdin.readline

N = int(input())
answer = [1] * N

weight_heights = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(weight_heights)):
    for j in range(len(weight_heights)):
        if i == j:
            continue
        cur_weight, cur_height = weight_heights[i]
        check_weight, check_height = weight_heights[j]
        if cur_weight < check_weight and cur_height < check_height:
            answer[i] +=1
print(" ".join(map(str, answer)))