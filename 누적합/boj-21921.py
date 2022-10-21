N , K = map(int, input().split())

numbers = list(map(int, input().split()))
# 최대값이 0이라면 sad를 프린트
if max(numbers) == 0:
    print("SAD")
else:
    # 첫 누적합을 초기화
    max_value = sum(numbers[0:K])
    prefix_sum = max_value
    cnt = 1
    for i in range(K, N):
        # 이터레이션을 돌면서 K개의 합을 구하기 위해서 현재 인덱스의 -K번째 수를 빼주고
        # 현재 인덱스를 더해준다.
        prefix_sum -= numbers[i-K]
        prefix_sum += numbers[i]
        # 현재의 K개의 합인 prefix가 max_value보다 크다면
        # cnt를 1로 초기화 해주고 max값을 업데이트 해준다.
        if prefix_sum > max_value:
            cnt = 1
            max_value = prefix_sum
        # prefix와 max가 같다면 갯수를 업데이트 해준다.
        elif prefix_sum == max_value:
            cnt += 1
    print(max_value)
    print(cnt)