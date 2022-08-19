from itertools import product
import sys
iter_num = int(sys.stdin.readline())
for _ in range(iter_num):
    cur_num = int(sys.stdin.readline())
    cnt = 0
    for i in range(1, 11):
        for j in product([1,2,3], repeat=i):
            if sum(j) == cur_num:
                cnt+=1
    print(cnt)