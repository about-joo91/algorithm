N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]

def is_target_square(r, c, weight):
    return graph[r][c] == graph[r+weight][c] == \
        graph[r][c+weight] == graph[r+weight][c+weight]

answer = 1
for r in range(N):
    for c in range(M):
        for weight in range(answer, max(N, M)):
            if r + weight >= N or c + weight >=M: continue
            if is_target_square(r, c,weight):
                answer = weight+1

print(answer**2)