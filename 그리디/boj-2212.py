N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))
dist = []

for i in range(1, N):
	dist.append(sensors[i] - sensors[i-1])

dist.sort()
print(sum(dist[:N-K]))
