import sys
input = sys.stdin.readline

N = int(input().rstrip())
drink = sorted(map(int, input().split()))
max_drink = drink[-1]

for i in range(N - 1):
	max_drink += (drink[i] / 2)

print(max_drink)
