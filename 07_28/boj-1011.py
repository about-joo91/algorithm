N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    distance = end - start
    move = 1
    sum_move = 0
    cnt = 0
    while sum_move < distance:
        cnt+=1
        sum_move += move
        if cnt %2 ==0:
            move +=1
    print(cnt)