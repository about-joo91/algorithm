N = int(input())
liquid = sorted(list(map(int, input().split())))
left = 0
right = N-1
min_value = int(10e9)
min_liquid = []
while left < right:
    status = liquid[left] + liquid[right]

    if abs(status) < min_value:
        min_liquid = [liquid[left], liquid[right]]
        min_value = abs(status)

    if status < 0:
        left +=1
    else:
        right-=1

print(*min_liquid)