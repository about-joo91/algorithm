N, M = map(int, input().split())

package_prices = []
each_prices = []
# 각 가격들을 리스트에 넣어서 최소 값을 뽑아준다.
for _ in range(M):
    package_price, each_price = map(int, input().split())
    package_prices.append(package_price)
    each_prices.append(each_price)

# 6개가 하나의 패키지이므로 6으로 나눈 값이 사야하는 패키지의 최소값이다.
# 패키지의 최소값이라는 표현을 사용한 이유는 기타줄을 여유분으로 사도 되기 때문이다.
package_cnt = N // 6
remain_cnt = N % 6

# 패키지로 살때와 낱개로 살때 가격의 최솟값을 각각 구해준다.
min_package = min(package_prices)
min_remain = min(each_prices)

# 갯수가 딱 맞게 패키지와 낱개를 양쪽다 구매할 경우와
# 여유분을 남기고 패키지만 구매하는 경우
# 낱개만 구매하는 경우 세가지 경우를 통틀어 최소값을 구해준다.
whole_pirce = min_package* package_cnt + min_remain * remain_cnt
package_only_price = min_package * (package_cnt+1)
remail_only_price = min_remain * N

print(min(whole_pirce, package_only_price, remail_only_price))