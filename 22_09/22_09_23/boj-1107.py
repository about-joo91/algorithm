import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken_btns = []
if M:
    broken_btns = list(map(int, input().split()))

min_count = abs(100 - N)

for num in range(1000000):
    num = str(num)
    
    for j in range(len(num)):
        if int(num[j]) in broken_btns:
            break
        elif j == len(num) -1:
            min_count = min(min_count, abs(int(num) - N) + len(num))
print(min_count)

#  부르트포스에 대한 이해가 조금 부족한 것 같다.

# 문제가 원하는 바가 부르트포스임을 이해한다고 해도 가능한 모든 경우를 완전탐색한다는 개념이 아직 머리에 익지 않은듯 하다.

# 그래서 바로 0 ~ 999999 까지 모두 탐색해서 최소차이를 업데이트한다는 생각에 접근하지 못했다.

# 문제를 더 많이 접하고 익숙해질 필요가 있어보인다.