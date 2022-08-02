from itertools import combinations
while True:
    selected_nums = list(map(int, input().split()))
    len_of_selected = selected_nums.pop(0)
    if len_of_selected == 0:
        break
    for lotto_num in sorted(list(combinations(selected_nums, 6))):
        print(' '.join(map(str, lotto_num)))
    print()
    