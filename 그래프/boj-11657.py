N, M = map(int, input().split())
INF= int(10e9)
times = [INF] * (N+1)
edges = []

for _ in range(M):
    start, end, time = map(int,input().split())
    edges.append((start, end, time))


def bellman_ford(start):
    times[start] = 0

    for i in range(N):
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            time = edges[j][2]

            if times[cur_node] != INF and times[next_node] > times[cur_node] + time:
                times[next_node] = times[cur_node] + time

                if i == N -1:
                    return True
    return False

negative_cycle = bellman_ford(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if times[i] == INF:
            print(-1)
        else:
            print(times[i])