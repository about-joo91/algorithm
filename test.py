import sys
sys.stdin = open('test.txt','r')

def delete_node(target):
    nodes[target] = -INF
    for idx in range(N):
        if target == nodes[idx]:
            delete_node(idx)


if __name__ == "__main__":
    N = int(input())
    nodes = list(map(int, input().split()))
    target_node = int(input())
    result = 0
    INF = 2

    delete_node(target_node)

    for i in range(N):
        if nodes[i] != -INF and i not in nodes:
            result+=1

    print(result)