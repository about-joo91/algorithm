import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
cnt = 0
while N > 0:
    N -=1
    size = 2 ** N
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        cnt += size ** 2
        c -= size
    elif r >= size and c < size:
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        cnt += size ** 2 * 3
        r -= size
        c -= size
print(cnt)