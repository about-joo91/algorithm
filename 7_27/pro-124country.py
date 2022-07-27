def solution(n):
    answer = ''
    Ternary = 3
    numbers = '124'
    while n:
        n-=1
        answer = answer + numbers[n%Ternary]
        n = n//3
    return answer[::-1]


print(solution(4))
