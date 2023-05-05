from collections import deque

N = int(input())
balloons = deque(input().split(' '))
locations = deque(range(1, N + 1))

while balloons:
    balloon = int(balloons.popleft())
    location = locations.popleft()

    print(location, end=" ")
    balloon = -(balloon - 1) if balloon > 0 else -balloon
    balloons.rotate(balloon)
    locations.rotate(balloon)
