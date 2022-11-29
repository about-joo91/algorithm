def backtracking(depth, limit, cur_seq):
    if depth == limit:
        print(*cur_seq[1:])
        return
    
    for number in sequential:
        if number not in cur_seq and cur_seq[-1] <= number:
            backtracking(depth+1, limit, cur_seq + [number])
        

while True:
    cur_input = list(map(int,input().split()))
    if cur_input[0] == 0:
        break
    
    N = cur_input[0]
    sequential = cur_input[1:]
    backtracking(0, 6, [-1])
    print()