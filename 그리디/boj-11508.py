import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse= True)
answer = 0
tmp = []
for i in range(1, N+1):
	if i % 3 == 0:
		answer += sum(tmp)
		tmp = []
	else:
		tmp.append(numbers[i-1])
print(answer + sum(tmp))
