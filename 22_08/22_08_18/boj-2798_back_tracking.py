import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
visited = [False] * (N+1)
sum_of_cards = []
answer = []
def dfs(depth, idx):
    if depth == 3:
        if sum(sum_of_cards) <= M:
            answer.append(sum(sum_of_cards))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            sum_of_cards.append(cards[i])
            dfs(depth+1, i+1)
            visited[i] = False
            sum_of_cards.pop()
            
dfs(0,0)
print(max(answer))