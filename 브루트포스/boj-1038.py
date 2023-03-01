import sys

def backtracking(cur_number, depth, limit):
    global answer

    if depth == limit:
        if answer == N:
            print("".join(map(str, cur_number)))
            sys.exit(0)
        answer +=1
        return

    for i in range(10):
        if len(cur_number) == 0:
            backtracking(cur_number+[i], depth+1,limit)
        elif cur_number[-1] > i:
            backtracking(cur_number+[i], depth+1,limit)

if __name__ == '__main__':
    N = int(input())
    answer = 0
    for i in range(1, 11):
        backtracking([], 0, i)

    print(-1)