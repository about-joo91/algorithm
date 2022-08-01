iter_num = int(input())
for _ in range(iter_num):
    H, W, N = map(int, input().split())
    num = 1
    breaker = False
    for w in range(1, W+1):
        for h in range(1, H+1):
            answer = ''
            if w // 10 < 1:
                answer = str(h)+ str(0)+str(w)
            else:
                answer = str(h)+str(w)
            if num == N:
                print(answer)
                breaker = True
                break
            num+=1
        if breaker:
            break