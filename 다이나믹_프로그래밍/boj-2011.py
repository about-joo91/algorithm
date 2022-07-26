import sys
password = input()

N = len(password)

# 암호 코드는 1 ~ 26이어야 하는데 시작값이 0이라면 암호화가 불가능하므로
# 첫값을 검사해 0이라면 불가능하다는 의미로 0을 프린트 해준다.
if password[0] == "0":
    print(0)
    sys.exit(0)

# 문제 예시에서 나와있는 25114로 예를 들면
# 첫번째 값이 0이 아님을 확인했기때문에 
# 첫번째값은 하나의 경우의수를 가지고 있기 때문에 1로 초기화 해준다.
dp = [0] * (N+1)
dp[0] = dp[1] = 1

# 따라서 두번째 값부터 검사를 하는데
# 밑의 식이 elif로 구분되어있지 않다는 점에 주목해야한다.
# 우선 지금 검사하고 있는 인덱스의 값이 0이 아니라면 경우의 수는 이전 인덱스 값과 동일하다.
# 예를들어 2, 5 까지 검사했을 때 새로운 경우의 수가 추가 된 것이 아니기 때문이다.
# 그러나 2와 5를 합친 수 25는 또 다른 알파벳을 형성하기 때문에 경우의 수가 하나 더 많아진다.
# 따라서 2와 5를 선택하기 이전 경우의 수를 더해 주어서 경우의 수를 더 추가해준다.
for i in range(2, N+1):
    if 9 < int(password[i-2]+password[i-1]) < 27:
        dp[i] += dp[i-2]
    if int(password[i-1]) > 0:
        dp[i] += dp[i-1]
print(dp[N] % 1000000)