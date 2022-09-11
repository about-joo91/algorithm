import sys
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort(reverse=True)
answer = numbers[0]

for i in range(1, N):
    answer = max(answer, numbers[i]*(i+1))

print(answer)