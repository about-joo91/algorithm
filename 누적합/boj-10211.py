T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    for i in range(1, N):
        if numbers[i-1] >= 0:
            numbers[i] = numbers[i] + numbers[i-1]
        max_value = max(max_value, numbers[i])
    print(max_value)