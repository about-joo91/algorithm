cnt = int(input())
N = list(map(int, input().split()))
if cnt ==1:
    print(N[0] ** 2)
else:
    print(max(N) * min(N))