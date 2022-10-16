N = int(input())

answers = []
# N번째 큰 수를 구해야 하기 때문에 그 이상의 수는 필요가 없다.
# 따라서 매번 소팅을 해주면서 필요한 만큼을 잘라주면
# 앞으로 소팅을 할때에도 크기가 점점 늘어나면서 N**2 만큼의 수를 돌면서 정렬을 할 필요가 없으므로
# 시간을 절약할 수 있다.
for _ in range(N):
    answers += list(map(int, input().split()))
    answers = sorted(answers, reverse=True)[:N]
print(answers[N-1])