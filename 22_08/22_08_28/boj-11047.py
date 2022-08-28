import sys
input = sys.stdin.readline
N, price = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.sort(reverse = True)

cnt = 0
i = 0
while price > 0:
    if price - coins[i] < 0:
        i+=1
        continue
    if price - coins[i] == 0:
        print(cnt+1)
        break
    price -= coins[i]
    cnt+=1