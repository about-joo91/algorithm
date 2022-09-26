N = int(input())
def solution(N):
    def get_partial_sum(num):
        ret = num
        while num > 0:
            ret += num % 10
            num //= 10
        return ret

    for i in range(N):
        if get_partial_sum(i) == N:
            return i
    return 0
print(solution(N))