N, K = map(int, input().split())
robots = [False] * N
belts = list(map(int, input().split()))

cnt = 0
while True:
    belts = [belts.pop()] + belts
    robots.pop()
    robots = [False] + robots
    robots[-1] = False

    for idx in range(len(robots)-1, -1, -1):
        if robots[idx] and belts[idx+1] > 0 and not robots[idx+1]:
            belts[idx+1] -= 1
            robots[idx] = False
            robots[idx+1] = True

    if belts[0] > 0:
        belts[0] -= 1
        robots[0] = True
        
    cnt+=1

    if belts.count(0) >= K:
        break
print(cnt)