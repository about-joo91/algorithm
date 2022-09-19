def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i ==0:
            return False
    return True

def solution(n, k):
    tmp = ''
    while n > 0:
        n , mod = divmod(n, k)
        tmp += str(mod)

    check_num = tmp[::-1].split('0')
    cnt = 0
    for num in check_num:
        if num.isdigit() and is_prime(int(num)):
                cnt+=1
    return cnt