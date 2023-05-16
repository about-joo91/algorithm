N = int(input())
numbers = [int(input()) for _ in range(N)][::-1]
answer = 0
for i in range(1, N):
    prev_num = numbers[i - 1]
    cur_num = numbers[i]
    
    diff = cur_num - (prev_num - 1)
    if diff <= 0: continue
    answer += diff
    numbers[i] = prev_num - 1

print(answer)
