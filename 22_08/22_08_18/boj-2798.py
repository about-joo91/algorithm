from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int,input().split()))
sum_of_comb = list(map(sum, list(combinations(cards, 3))))
less_M = list(filter(lambda x: x <= M , sum_of_comb))
print(max(less_M))
