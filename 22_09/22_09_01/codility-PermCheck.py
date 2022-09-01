def solution(A):
    A = sorted(A)
    if A[0] != 1:
        return 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] != 1:
            return 0
    return 1