from itertools import combinations

N, M = map(int, input().split())
candidates = list(range(1, N+1))
for comb in list(combinations(candidates, M)):
    print(' '.join(map(str, comb)))