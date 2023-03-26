def is_in_partial_arr(partial_arr, target):
    left = 0
    right = len(partial_arr)-1
    while left < right:
        sum_of_two_number = partial_arr[left] + partial_arr[right]
        if sum_of_two_number == target:
            return True
        elif sum_of_two_number > target:
            right -= 1
        else:
            left += 1
    return False
N = int(input())
numbers = sorted(list(map(int, input().split())))

answer = 0
for i in range(N):
    if is_in_partial_arr(numbers[:i] + numbers[i+1:], numbers[i]):
        answer+=1

print(answer)