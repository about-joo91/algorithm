import sys
input = sys.stdin.readline
split_minus = input().split('-')
answer = sum(map(int,split_minus[0].split("+")))
for math in split_minus[1:]:
    answer -= sum(map(int,math.split('+')))
print(answer)