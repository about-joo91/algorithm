N, L = map(int,input().split())
holes = sorted(list(map(int, input().split())))

before = holes[0]
end = holes[0]+ L
cnt = 1

for i in range(N):
    if before <= holes[i] < end: continue
    else:
        before = holes[i]
        end = holes[i] + L
        cnt += 1

print(cnt)