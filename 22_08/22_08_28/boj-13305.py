import sys
input = sys.stdin.readline
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = 0
pre_price = prices[0]
for i in range(N-1):
    if prices[i] < pre_price:
        pre_price = prices[i]
    answer += pre_price * distances[i]
print(answer)