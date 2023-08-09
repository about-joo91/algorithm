import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def gcd(num1, num2):
	while num2 > 0:
		num1, num2 = num2, num1 % num2
	return num1


print(M - gcd(N, M))
