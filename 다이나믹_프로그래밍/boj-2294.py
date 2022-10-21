cnt_of_coins,target = map(int,input().split())
coins = [int(input()) for _ in range(cnt_of_coins)]
INF = 1e9
coin_cnt_by_number = [INF] * (target +1)

coin_cnt_by_number[0] = 0
# 코인들을 전체 순회하면서 코인값을 가져온다.
# 가져온 코인을 통해서 타겟까지 다시 순회를 통해서
# 지금 코인이 만약 1이라면 1~target까지 coin_cnt_by_number의 현재 조회중인 테이블과
# 이전 테이블의 값 +1을 비교하여 작은 값으로 업데이트 해준다.
# 이렇게 순회를 마치고 나서 코인들로 만들 수 없다면 초기 설정값 INF가 그대로 남아있기 때문에 -1을 프린트해주고
# 값이 있다면 최소값으로 설정이 되었기 때문에 coin_cnt_by_number의 인덱스가 target인 값을 프린트 해준다.
for coin in coins:
    for number in range(coin, target+1):
        coin_cnt_by_number[number] = min(coin_cnt_by_number[number-coin] +1, coin_cnt_by_number[number])
if coin_cnt_by_number[target] == INF:
    print(-1)
else: print(coin_cnt_by_number[target])