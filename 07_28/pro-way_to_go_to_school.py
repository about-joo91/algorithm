def solution(m, n, puddles):
    # 0,0 에서 출발한다 dp의 값은 0이다
    # 오른쪽과 아래로 이동한다. 이때 거리는 dp+1이다
    # 오른쪽으로 갈 때는 m을 넘지 않고 아래로 갈 때는 n을 넘지 않는 선에서 이동한다.
    # map table과 dp 테이블이 따로 있다.
    # 다음 이동할 곳을 찾는다 이동 후에 전 거리값을 찾은 다음에 1을 더한다
    # 지금 dp 테이블에 값이 이미 있다면 최소값을 dp테이블 값으로 취한다.
    map = [[0] * m for _ in range(n)]
    dp = [[] *m for _ in range(n)]
    directions = [[0, 1], [1, 0]]
    for puddle in puddles:
        map[puddle[0]-1][puddle[1]-1] = 1
    dp_num = 0


solution(4,3,[[2, 2]])