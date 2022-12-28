from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
max_value = 0
for element in list(permutations(numbers, N)):
    cur_num = 0
    for i in range(len(element)-1):
        cur_num += abs(element[i] - element[i+1])
    if cur_num > max_value:
        max_value = cur_num

print(max_value)



def permute(depth, elements):
    global max_value
    if depth == N:
        cur_num = 0
        for i in range(N-1):
            cur_num += abs(elements[i] - elements[i+1])
        max_value = max(max_value, cur_num)

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            permute(depth+1, elements + [numbers[idx]])
            visited[idx] = False


visited = [False] * N

permute(0, [])
print(max_value)