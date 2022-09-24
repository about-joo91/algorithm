import sys
input= sys.stdin.readline

N = int(input())
cnt = 1
cur_num = 1
for i in range(N // 6+1):
    cur_num += (6 *i)
    if cur_num >= N:
        break
    cnt+=1
print(cnt)