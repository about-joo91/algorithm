import sys
def gcd(A,B):
    while B >0:
        A, B = B, A%B
    return A

iter_num = int(sys.stdin.readline())
for _ in range(iter_num):
    first, second = map(int, sys.stdin.readline().split())
    if first < second:
        first, second = second, first
    print(first * second // gcd(first,second))