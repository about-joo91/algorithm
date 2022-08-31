import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    len_of_stock = int(input())
    stocks = list(map(int, input().split()))
    answer = 0
    max_stock = 0
    for stock in reversed(stocks):
        max_stock = max(max_stock, stock)
        if stock < max_stock:
            answer += (max_stock-stock)
    print(answer)