import sys
input = sys.stdin.readline
N, M = map(int, input().split())

S = set([input() for _ in range(N)])
cnt = 0
for i in range(M):
    check_str = input()
    if check_str in S:
        cnt+=1
print(cnt)