import sys
input= sys.stdin.readline
N = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))

for i in range(N-1, 0, -1):
    if numbers[i-1] > numbers[i]:
        target = i - 1
        break
else:
    print(-1)
    sys.exit(0)

for i in range(N-1, 0, -1):
    if numbers[i] < numbers[target]:
        numbers[target], numbers[i] = numbers[i], numbers[target]
        break
answer= numbers[:target+1]+ sorted(numbers[target+1:], reverse=True)

print(*answer)