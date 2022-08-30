import sys
input = sys.stdin.readline
target, cur_num = map(int, input().split())
cnt = 0
while target < cur_num:
    if cur_num % 2 == 0:
        cur_num //= 2
    elif str(cur_num)[-1] == '1':
        cur_num = int(str(cur_num)[:-1])
    else:
        print(-1)
        break
    cnt+=1
    if cur_num == target:
        print(cnt+1)
        break
else:
    print(-1)