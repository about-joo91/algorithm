def is_possible_to_make_arch(cur_str):
    stack = []
    for i in range(len(cur_str)):
        if stack and stack[-1] == cur_str[i]:
            stack.pop()
        else: stack.append(cur_str[i])
    return False if stack else True


if __name__ == "__main__":
    N = int(input())
    cnt = 0

    for _ in range(N):
        cur_str = input()
        if len(cur_str) % 2 != 0: continue
        if not is_possible_to_make_arch(cur_str): continue
        cnt+=1

    print(cnt)