import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] * 10001
for _ in range(N):
    cur_num = int(input())
    numbers[cur_num] +=1

for i in range(len(numbers)):
    for _ in range(numbers[i]):
        print(i)