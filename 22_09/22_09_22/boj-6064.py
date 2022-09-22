import sys
input = sys.stdin.readline


T = int(input())


for _ in range(T):
    N, M, x, y = map(int, input().split())
    
    while x <= N* M:
        if (x - y) % M == 0:
            print(x)
            break
        x += N
    else:
        print(-1)