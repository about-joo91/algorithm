import sys
input = sys.stdin.readline

N, M = map(int, input().split())
video_data = list(map(int, input().split()))

max_size = max(video_data)
left = max_size
right = sum(video_data)
answer = int(10e9)

while left <= right:
    mid = (left + right)//2
    cnt = 1
    cur_size = 0
    idx = 0
    while cnt <= M and idx < N:
        if (cur_size + video_data[idx]) <= mid:
            cur_size += video_data[idx]
        else:
            cnt+=1
            cur_size = video_data[idx]
        idx+=1
    if cnt > M:
        left = mid+1
    else:
        right = mid-1
        answer = min(answer, mid)

print(answer)