import copy

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
rotations = [list(map(int, input().split())) for _ in range(K)]
answer = int(10e9)

def rotate(r, c, s, arr):
    mr = r - s - 1
    mc = c - s - 1
    Mr = r + s - 1
    Mc = c + s - 1
    tmp = arr[mr][mc]

    for i in range(mr, Mr):
        arr[i][mc] = arr[i+1][mc]

    for i in range(mc, Mc):
        arr[Mr][i] = arr[Mr][i+1]

    for i in range(Mr, mr, -1):
        arr[i][Mc] = arr[i-1][Mc]

    for i in range(Mc, mc, -1):
        arr[mr][i] = arr[mr][i-1]
    
    arr[mr][mc+1] = tmp

def backtracking(depth, orders):
    global answer
    if depth == K:
        copied_graph = copy.deepcopy(graph)
        for order in orders:
            r, c, s = rotations[order]
            while s > 0:
                rotate(r,c,s,copied_graph)
                s-=1
        arr_value = min(map(sum, copied_graph))
        answer = min(answer, arr_value)
        return
    
    for i in range(K):
        if i not in orders:
            orders.append(i)
            backtracking(depth+1, orders)
            orders.pop()

backtracking(0, [])
print(answer)