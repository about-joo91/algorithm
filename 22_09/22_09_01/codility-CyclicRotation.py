def solution(A, K):
    for _ in range(K):
        A = A[-1:] + A[:-1]
    return A