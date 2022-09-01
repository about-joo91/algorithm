def solution(A):
    A = sorted(list(set(list(filter(lambda x: x>0, A)))))
    for idx, num in enumerate(A):
        if idx+1 != num:
            return idx+1
    return len(A)+1