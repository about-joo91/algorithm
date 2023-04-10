import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    numbers[i] += numbers[i-1]

M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    print(numbers[end] - numbers[start-1])