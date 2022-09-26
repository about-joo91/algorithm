import sys
input= sys.stdin.readline

L = int(input().rstrip())
alphas = input().rstrip()
ord_condition = 96
answer = 0
for idx, alpha in enumerate(alphas):
    answer += (ord(alpha) - ord_condition) * (31 **idx)
print(answer % 1234567891)