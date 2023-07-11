def find_parents(cur_node):
    result = []
    while cur_node:
        result.append(cur_node)
        cur_node = parents[cur_node]
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    parents = [0] * (N+1)
    for _ in range(N-1):
        parent, child = map(int, input().split())
        parents[child] = parent

    node_1, node_2 = map(int, input().split())
    if node_1 == node_2:
        print(parents[node_1])
        continue
    parents1 = find_parents(node_1)
    parents2 = find_parents(node_2)
    for parent in parents1:
        if parent in parents2:
            print(parent)
            break