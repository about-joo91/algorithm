N = int(input())
numbers = list(map(int, input().split()))

dp = [numbers[0]]

def get_bisec_left(target):
    left = 0
    right = len(dp)
    while left <= right:
        mid = (left + right)//2
        if dp[mid] < target:
            left = mid+1
        else: right= mid-1
    return left


for i in range(1, N):
    if numbers[i] > dp[-1]:
        dp.append(numbers[i])
    else:
        idx = get_bisec_left(numbers[i])
        dp[idx] = numbers[i]

print(len(dp))
