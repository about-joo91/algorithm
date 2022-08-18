import sys

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int,input().split()))
sum_of_comb = list(map(sum, list(combinations(cards, 3))))
less_M = list(filter(lambda x: x <= M , sum_of_comb))
print(max(less_M))



N, M = map(int, input().split())
cards = list(map(int,input().split()))
visited = [False] * (N+1)
sum_of_cards = []
answer = []
def dfs(depth, idx, cards):
    if depth == 3 and sum(sum_of_cards) <= M:
        answer.append(sum(sum_of_cards))
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            sum_of_cards.append(cards[i])
            dfs(depth+1, i+1)
            visited[i] = False
            sum_of_cards.pop()
            
dfs(0,0, cards)
print(max(answer))