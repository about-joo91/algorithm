def get_count_of_armor():
    left = 0
    right = len(materials)-1

    cnt = 0
    while left < right:
        sum_of_material = materials[left] + materials[right]
        if sum_of_material == target:
            cnt+=1
        if sum_of_material < target:
            left+=1
        else:
            right-=1
    return cnt

N = int(input())
target = int(input())
materials = sorted(list(map(int, input().split())))

count_of_armor = get_count_of_armor()
print(count_of_armor)
