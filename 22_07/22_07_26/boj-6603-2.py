def combinations(array, num):
    result = []
    if num == 0:
        return [[]]
    
    for idx, elem in enumerate(array):
        for others in combinations(array[idx+1:],num-1):
            result.append([elem] + others)
    return result

while True:
    selected_nums = list(map(int, input().split()))
    len_of_selected = selected_nums.pop(0)
    if len_of_selected == 0:
        break
    for lotto_num in sorted(list(combinations(selected_nums, 6))):
        print(' '.join(map(str, lotto_num)))
    print()
    