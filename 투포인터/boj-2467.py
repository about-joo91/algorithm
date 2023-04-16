N = int(input())
materials = list(map(int, input().split()))

def get_idx_of_smallest_sum():
    left = 0
    right = N-1
    smallest_sum = int(10e9)
    left_idx, right_idx = 0, 0

    while left < right:
        cur_sum = materials[left] + materials[right]
        if abs(cur_sum) < smallest_sum:
            smallest_sum = abs(cur_sum)
            left_idx = left
            right_idx = right
        
        if cur_sum < 0:
            left +=1
        else: right-=1
    return[left_idx, right_idx]

left_idx, right_idx = get_idx_of_smallest_sum()
print(materials[left_idx], materials[right_idx])