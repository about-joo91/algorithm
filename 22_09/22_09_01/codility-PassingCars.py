def solution(A):
    sums = []
    cur_sum = 0
    answer = 0
    limit = int(1e9)
    for num in A:
        cur_sum += num
        sums.append(cur_sum)
    for i in range(len(A)):
        if A[i] == 0:
            answer += (sums[len(A)-1] - sums[i])
    return answer if answer <= limit else -1