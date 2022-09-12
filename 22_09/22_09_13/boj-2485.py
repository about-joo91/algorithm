import sys

input = sys.stdin.readline
N = int(input())
trees = [int(input()) for _ in range(N)]
intervals = []

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a%b)

for i in range(1, N):
    intervals.append(trees[i] - trees[i-1])

gcd = intervals[0]
for i in range(1, len(intervals)):
    gcd = get_gcd(gcd, intervals[i])

answer = 0
for interval in intervals:
    answer += (interval// gcd -1)
print(answer)