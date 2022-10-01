def solution(n, s):
    if n > s: return [-1]
    
    start = s // n
    answer = [start] * n
    idx = n - 1
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1
    return answer