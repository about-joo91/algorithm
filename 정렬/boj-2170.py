N = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

start = lines[0][0]
end = lines[0][1]
answer = 0

for i in range(1, N):
    cur_start, cur_end = lines[i]
    print(cur_start, cur_end)

    if end > cur_start:
        end = max(cur_end, end)
    else:
        answer += (end - start)
        start = cur_start
        end = cur_end

print(answer + (end - start))
