N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = 0
cnt = 0

cur_num = numbers[0]
while right < N:
    if cur_num > M:
        cur_num -= numbers[left]
        left +=1
    elif cur_num == M:
        cnt+=1
        cur_num -= numbers[left]
        left+=1
    else:
        right+=1
        if right >= N:
            break
        cur_num += numbers[right]


print(cnt)