N, D = map(int, input().split())

distances = [x for x in range(D+1)]

vertex = [list(map(int, input().split())) for _ in range(N)]

for i in range(D+1):
    if i > 0:
        # 현재의 거리값과 이전 거리값 +1을 비교하여 최소값으로 업데이트 해준다.
        # distances는 0부터 D까지 하나씩 증가하는 숫자로 초기화 되어있다.
        # 따라서 지름길이 업데이트가 된 부분, 이전값 +1을 비교하면 지름길로 가는게 빠를지
        # 길을 따라 오는게 빠를지 알 수 있다.
        distances[i] = min(distances[i], distances[i-1]+1)
    # vertex를 순회하면서 만약에 현재 인덱스와 일치하는 start값이 있다면
    # end가 D보다 작은지 검사하고 지름길이 더 빠른길이라면 값을 업데이트 해준다.
    for start, end, distance in vertex:
        if i == start and end <= D and distances[i]+ distance < distances[end]:
            distances[end] = distances[i] + distance
print(distances[D])