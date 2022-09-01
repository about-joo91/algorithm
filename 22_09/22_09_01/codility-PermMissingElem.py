def solution(A):
    A = sorted(A)
    if len(A) == 0:
        return 1
    for i in range(1, len(A)+1):
        if A[i-1] != i:
            return i
    return len(A) +1