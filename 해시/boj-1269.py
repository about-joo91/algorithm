N, M = map(int, input().split())
fir_set = set(list(map(int, input().split())))
sec_set = set(list(map(int, input().split())))

print(len(fir_set - sec_set) +len(sec_set - fir_set))


N, M = map(int, input().split())

set_map = {}

fir_num = list(map(int, input().split()))
for i in range(N):
    set_map[fir_num[i]] = 1

sec_nums = list(map(int, input().split()))
for sec_num in sec_nums:
    if sec_num in set_map:
        set_map[sec_num] -= 1
    else: set_map[sec_num] = 1

print(sum(set_map.values()))