N, M = map(int, input().split())
dnas = [input() for _ in range(N)]
hamming_distances = [0] * N

result = ""
cnt = 0

for i in range(M):
    alpha = [0] * 26
    for j in range(N):
        alpha[ord(dnas[j][i]) - 65]+=1
    result += chr(alpha.index(max(alpha)) + 65)
    
for i in range(N):
    for j in range(M):
        if dnas[i][j] != result[j]:
            cnt += 1
print(result)
print(cnt)