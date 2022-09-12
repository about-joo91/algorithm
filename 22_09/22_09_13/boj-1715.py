import heapq
import sys

input = sys.stdin.readline
N = int(input())
cards = []
answer = 0


for _ in range(N):
    heapq.heappush(cards, int(input()))
answer = 0
while len(cards)!=1:
    first_value = heapq.heappop(cards)
    second_value = heapq.heappop(cards)
    answer += (first_value+second_value)
    heapq.heappush(cards, first_value+second_value)
print(answer)