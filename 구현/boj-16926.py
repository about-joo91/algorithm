import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        value = arr[x][y]

        for j in range(i + 1, N - i):
            x = j
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        for j in range(i + 1, M - i):
            y = j
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        for j in range(i + 1, N - i):  # 우
            x = N - j - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        for j in range(i + 1, M - i):
            y = M - j - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

for i in arr:
    print(*i)
