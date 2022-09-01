def solution(X, Y, D):
    diff = Y - X
    if diff == 0:
        return 0
    if diff % D ==0:
        return diff // D
    answer = diff // D +1
    return answer