N = int(input())
numbers = sorted(list(map(int, input().split())))
target = int(input())

cnt = 0
left = 0
right = N-1

while left < right:
    cur_sum = numbers[left] + numbers[right]
    if cur_sum == target:cnt+=1
    if cur_sum > target:
        right -=1
    else:
        left+=1

print(cnt)