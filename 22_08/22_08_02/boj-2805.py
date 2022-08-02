N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

result = 0
while start <= end:
    mount = 0
    mid = (start + end) //2
    for tree in trees:
        if tree > mid:
            mount+=(tree - mid)
    if mount < M:
        end = mid -1
    else:
        result = mid
        start = mid +1
print(result)