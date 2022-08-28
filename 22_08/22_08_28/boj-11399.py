import sys
input = sys.stdin.readline
N = int(input())
lines = list(map(int, input().split()))
lines.sort()
waits = 0
answer = 0
for line in lines:
    waits += line
    answer += waits
print(answer)