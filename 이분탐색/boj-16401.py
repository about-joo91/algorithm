def can_share(x):
    if x == 0: return True
    cnt = 0
    for i in range(N):
        cnt += (snacks[i] // x)
    return cnt >= M

if __name__ == '__main__':
    M, N = map(int, input().split())

    snacks = list(map(int, input().split()))
    left, right = 1, max(snacks)
    result = 0
    while left <= right:
        mid = (left + right)//2
        if can_share(mid):
            left = mid +1
            result = mid
        else:
            right = mid -1
    print(result)