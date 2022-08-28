import sys
input = sys.stdin.readline
N = int(input())
fir_arr = sorted(list(map(int, input().split())), reverse = True)
sec_arr = sorted(list(map(int, input().split())))
answer = 0

for i in range(N):
    answer += fir_arr[i] * sec_arr[i]
print(answer)
