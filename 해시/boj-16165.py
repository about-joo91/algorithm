N, M = map(int, input().split())
groups_member_map = {}
member_groups_map = {}
for _ in range(N):
    group_name = input()
    groups_member_map[group_name] = []
    member_count = int(input())
    for _ in range(member_count):
        member_name = input()
        groups_member_map[group_name].append(member_name)
        member_groups_map[member_name] = group_name

for _ in range(M):
    test_name = input()
    test_number = int(input())
    if test_number == 0:
        print('\n'.join(sorted(groups_member_map[test_name])))
    else:
        print(member_groups_map[test_name])