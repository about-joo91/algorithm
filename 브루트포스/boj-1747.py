N = int(input())

primes = []
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** (1/2))+1):
        if number % i == 0:
            return False
    return True

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

while True:
    if is_prime(N):
        if is_palindrome(N):
            print(N)
            break
    N+=1