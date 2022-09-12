N = int(input())
budgets = list(map(int,input().split()))
limit = int(input())

start, end = 0, max(budgets)
while start <= end:
    mid = (start + end) // 2
    num = 0
    for budget in budgets:
        if mid <= budget: num += mid
        else: num += budget
    if num <= limit: start = mid+1
    else: end = mid - 1

print(end)