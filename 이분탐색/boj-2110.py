import sys
input = sys.stdin.readline

N, M = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

left, right = 0, houses[-1]


while left <= right:
    prev_house_num = 0
    cnt = 1

    mid = (left + right) // 2
    
    for i in range(1, N):
        if houses[i] - houses[prev_house_num] >= mid:
            prev_house_num = i
            cnt+=1
            
    if cnt >= M:
        left = mid + 1
    else: right = mid - 1

print(right)