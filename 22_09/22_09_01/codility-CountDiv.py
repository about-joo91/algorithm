def solution(A, B, K):
    if A == 0:
        return B//K +1
    return B//K -(A-1)//K