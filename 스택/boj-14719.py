H, W = map(int, input().split())
cities = list(map(int, input().split()))

stack = []
answer = 0

for idx in range(W):
    while stack and cities[stack[-1]] < cities[idx]:
        prev_city = stack.pop()
        if not stack: break
        distance = (idx - stack[-1]) - 1
        height = min(cities[stack[-1]], cities[idx]) - cities[prev_city]
        answer += (height * distance)
    stack.append(idx)

print(answer)