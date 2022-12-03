def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n, m = map(int, input().split())

int(factorial(n) / (factorial(n-m)*factorial(m)))