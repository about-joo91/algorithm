# 소수라면 가짜소수가 아니기 때문에 소수인지 검증해준다.
def is_prime(number):
    if number == 1:
        return False
    for i in range(2,int(number **(1/2))+1):
        if number % i == 0:
            return False
    return True
# 받아온 수의 최대로 10억 제곱까지 계산해야하므로
# 분할정복으로 해결한다. 
# 재귀 함수를 통해서 스택을 계속 쌓아가면서
# 제곱 연산을 마친 값을 가져와 x 변수에 담아준다.
# 현재 지수가 홀수라면 x의 제곱 * 밑 값을 반환하고
# 짝수라면 x의 제곱을 반환한다.
# 추가로 문제에서 요구한 지수값의 나머지를 제일 마지막에 구하면
# 메모리 초과가 날 수 있다. 따라서 mod라는 매개변수로 받아와 나머지를 연산마다 구해준다.
def fpow(number,square, mod):
    if square == 1:
        return number
    else:
        x = fpow(number, square//2, mod)
        if square % 2 == 0:
            return x * x % mod
        else: return x * x * number % mod

# squre값이 소수라면 no
# number의 square제곱의 % square 연산이 number와 같다면 yes
# 아니라면 no
def is_fake_prime(number, square):
    if is_prime(square):
        return "no"
    check_needed_number = fpow(number,square, square) % square
    if check_needed_number == number:
        return "yes"
    else: return "no"
    
    
while True:
    square, number = map(int, input().split())
    if square == 0:
        break
    print(is_fake_prime(number, square))