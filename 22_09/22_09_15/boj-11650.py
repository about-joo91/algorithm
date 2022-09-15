import sys

input = sys.stdin.readline
N  = int(input())
answers = []
for _ in range(N):
    answers.append(list(map(int,input().split())))
answers.sort(key=lambda x:(x[0], x[1]))

for answer in answers:
    print(f"{answer[0]} {answer[1]}")