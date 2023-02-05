import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))

def bisect_left(arr: list[int], number: int) -> int:
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < number: left = mid+1
        else: right = mid
    return left
dp = [numbers[0]]
for i in range(1, N):
    if numbers[i] > dp[-1]:
        dp.append(numbers[i])
    else:
        idx = bisect_left(dp, numbers[i])
        dp[idx] = numbers[i]

print(len(dp))