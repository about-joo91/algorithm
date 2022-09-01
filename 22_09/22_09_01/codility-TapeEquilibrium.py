def solution(A):
    left = A[0]
    right = sum(A[1:])
    minimum = abs(right- left)
    for i in range(1, len(A)-1):
        left += A[i]
        right -= A[i]
        minimum  = min(minimum,  abs(right- left))
    return minimum