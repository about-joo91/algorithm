N = int(input())
numbers = list(map(int, input().split()))

is_next = False
for i in range(N-1, 0,-1):
    if numbers[i-1] < numbers[i]:
        for j in range(N-1, 0, -1):
            if numbers[i-1] < numbers[j]:
                numbers[j], numbers[i-1] = numbers[i-1], numbers[j]
                numbers = numbers[:i] + sorted(numbers[i:])
                is_next = True
                break
    if is_next:
        print(*numbers)
        break
else:
    print(-1)