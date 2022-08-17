"""
1계단 혹은 2계단을 오를 수 있다. 

연속된 3계단을 밟을 수 없다. => 이 의미는 1계단씩 세번은 오를 수 없다는 것
각 dp테이블 마다 최근 2계단의 정보를 저장한다.
그 2계단과 지금 올라가려고 하는 계단이 모두 1로 일치하면 continue
insert와 pop을 활용하면 최근 계단을 계속 업데이트해줄 수 있다.

만약 dp리스트의 len이 3보다 낮으면 1번 인덱스에 인설트만 해준다.
0번째 인덱스에는 값을 넣고 1번째인덱스에 전값 2번째 인덱스에 전전값을 넣는다고 하면
0번을 max()를 이용하여 항상 맥스값으로 바꿔주고
1번에 이번값을 insert해준다.
dp[1].pop()을 하여 전전전 값을 빼준다.

마지막 계단은 반드시 밟아야 한다.
"""

import sys
stair_cnt = int(sys.stdin.readline())
dp = [0 for _ in range(301)]
stairs = [0 for _ in range(301)]
for i in range(stair_cnt):
    stairs[i] = int(sys.stdin.readline())
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])
for i in range(3, stair_cnt):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], stairs[i]+ dp[i-2])
print(dp[stair_cnt-1])