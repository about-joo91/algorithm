import sys
input = sys.stdin.readline
N, price = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for i in reversed(range(N)):
    cnt += price //coins[i]
    price = price % coins[i]
print(cnt)