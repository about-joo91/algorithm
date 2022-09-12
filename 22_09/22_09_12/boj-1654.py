N , K = map(int, input().split())
lans = [int(input()) for _ in range(N)]

start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    
    
    for lan in lans:
        lines += (lan//mid)
        
    if lines >= K: start  = mid + 1
    else: end = mid - 1
print(end)