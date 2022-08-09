def solution(people, limit):
    people.sort()
    small, big = 0, len(people)-1
    cnt = 0
    while small <= big:
        cnt+=1
        if people[small] + people[big] <= limit:
            small +=1
        big -=1
    return cnt
    
print(solution([70, 80, 50],100))