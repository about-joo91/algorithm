
N, M = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1
print(happiness)