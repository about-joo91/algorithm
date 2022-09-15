from collections import deque
import sys

input = sys.stdin.readline
N  = int(input())

cards = deque(list(range(1, N+1)))

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.popleft())