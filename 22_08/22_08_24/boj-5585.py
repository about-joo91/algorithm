import sys
input = sys.stdin.readline
coins = [500, 100, 50, 10, 5, 1]
price = 1000 - int(input())
cnt = 0
pointer = 0
while True:
    if price - coins[pointer] < 0:
        pointer+=1
    else:
        price -= coins[pointer]
        cnt+=1
    if price == 0:
        break
print(cnt)