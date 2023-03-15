N = int(input())

numbers = list(map(int, input().split()))
visited = [False] * N
answers = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if visited[j]: continue
        if cnt == numbers[i]:
            visited[j] = True
            answers[j] = (i+1)
            break
        cnt+=1

print(*answers)