N, K = map(int, input().split())

numbers = list(map(int, input().split()))

check_number = numbers[0]
left = 0
right = 0
minus_inf = -int(10e9)
answer = minus_inf

while right < N and left <= right:
    if right - left != K-1:
        right+=1
        check_number += numbers[right]
        continue
    answer = max(answer, check_number)
    if right == N-1:
        break
    right+=1
    check_number += numbers[right]
    check_number -= numbers[left]
    left += 1
    
print(answer)