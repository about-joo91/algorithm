import sys
N, S = map(int, sys.stdin.readline().split())
subsequence = list(map(int, sys.stdin.readline().split()))
cnt = 0

def find_subsequence(idx, sum_sub):
    global cnt
    if idx >= N:
        return
    sum_sub += subsequence[idx]
    if S == sum_sub:
        cnt +=1
    find_subsequence(idx +1, sum_sub)

    find_subsequence(idx+1, sum_sub - subsequence[idx])

find_subsequence(0,0)
print(cnt)