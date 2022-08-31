import sys
input = sys.stdin.readline
N, K = map(int, input().split())
plugs = list(map(int, input().split()))
concents = []
cnt = 0
for idx, plug in enumerate(plugs):
    if plug in concents:
        continue
    if len(concents) < N:
        concents.append(plug)
        continue
    check_idx = []
    for concent in concents:
        after_this = plugs[idx+1:]
        if concent in after_this:
            check_idx.append(after_this.index(concent))
        else:
            check_idx.append(101)
    del concents[check_idx.index(max(check_idx))]
    concents.append(plug)
    cnt +=1
print(cnt)