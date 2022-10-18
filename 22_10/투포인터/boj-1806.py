length, condition = map(int, input().split())

sequence = list(map(int, input().split()))
# length의 조건이 1000000 이므로 최대값을 그보다 1 크게 설정했다.
INF = 1000001
def get_less_cnt_of_sum(INF):
    
    right=0
    left=0
    answer = INF
    prefix = sequence[0]

    while True:
        # prefix값을 계속해서 업데이트 해주는데 그 값이 조건값보다 작으면
        # 다음 값을 더해야 하므로 오른쪽 포인터에 1을 더해주고 그 다음 값을 더해서 prefix를 업데이트 해준다.
        if prefix < condition:
            right+=1
            if right == length:
                break
            prefix += sequence[right]
        else:
            # 만약 두 값이 같아진다면 두 포인터가 가르키는 인덱스의 단일값이 조건보다 크거나 같다는 의미로
            # 1을 리턴해준다.
            if right == left:
                return 1
            # 만약 prefix가 조건보다 크거나 같으면 answer에 거리값을 업데이트 해주고
            # 왼쪽 포인터 그러니까 현재 인덱스로부터 먼 값부터 가까운 값까지 하나씩 빼주면
            # 최소 누적합을 구할 수 있다. 
            answer = min(answer, right-left+1)
            prefix -= sequence[left]
            left+=1
    return answer


answer = get_less_cnt_of_sum(INF)
# 반환된 answer가 초반에 설정한 INF값과 동일하다면 값은 업데이트 되지 않은 것이므로 합으로 조건에 부합하는 값을 찾을 수 없다는 의미이다.
# 따라서 0을 프린트해주고 아니라면 answser를 프린트해주면 된다.
if answer == INF: print(0)
else: print(answer)