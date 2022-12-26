import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())

def find_parent(number):
    if number == multi_set[number]:
        return number
    parent = find_parent(multi_set[number])
    multi_set[number] = parent
    return multi_set[number]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return 
    if a < b:
        multi_set[b] = a
    else: multi_set[a] = b

multi_set = [i for i in range(N+1)]
for _ in range(M):
    operator, fir_num, sec_num = map(int, input().split())
    if operator == 0:
        union(fir_num, sec_num)
    else:
        if find_parent(fir_num) == find_parent(sec_num):
            print("YES")
        else:
            print("NO")
        
