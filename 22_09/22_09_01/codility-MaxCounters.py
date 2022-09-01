def solution(N, A):
    answer = [0] * N
    max_num = 0
    max_tmp = 0
    for num in A:
        if num <= N:
            if answer[num-1] < max_num:
                answer[num-1] = max_num
            answer[num-1] +=1
            max_tmp = max(answer[num-1], max_tmp)
        else:
            max_num = max_tmp
    for i in range(N):
        if answer[i] < max_num:
            answer[i] = max_num
    return answer