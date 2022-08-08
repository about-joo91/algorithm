def bino(N, K):
    if K > N:
        return 0
    if K == 0 or K == N:
        return 1
    
    return bino(N-1, K-1) + bino(N-1, K)

N, K = int(input().split())

print(bino(N, K))

