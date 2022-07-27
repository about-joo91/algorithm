iter_num = int(input())
cnt = 0
for _ in range(iter_num):
    check_stack = []
    might_be_group = input()
    for idx, alpha in enumerate(might_be_group):
        if alpha not in check_stack:
            check_stack.append(alpha)
        elif alpha in check_stack and might_be_group[idx-1] != alpha:
            cnt -=1
            break
        else:
            continue
    cnt+=1
print(cnt)