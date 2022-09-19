def solution(n, info):
    answer = [0 for _ in range(11)]
    tmp = [0 for _ in range(11)]
    max_diff = 0
    
    for subset in range(1, 1<<10):
        ryan = 0
        apeach = 0
        cnt = 0
        
        for i in range(10):
            if subset & (1 << i):
                ryan += 10 - i
                tmp[i] = info[i]+1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    apeach += 10 - i
                    
        if cnt > n: continue
        
        tmp[10] = n - cnt
        
        if ryan - apeach == max_diff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    max_diff = ryan - apeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        
        if ryan - apeach > max_diff:
            max_diff = ryan - apeach
            answer = tmp[:]
            
    if max_diff == 0:
        answer = [-1]
    return answer


