import sys
input = sys.stdin.readline

numbers = [True] * (10001)
numbers[0] = numbers[1] = False
    
for i in range(2, 10001):
    for j in range(i*2, 10001, i):
        numbers[j] = False

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    idx = n // 2
    while n - idx > 0:
        is_break = False
        while not numbers[idx]:
            idx +=1
        
        if numbers[n - idx]:
            print(n - idx, idx)
            is_break = True
            break
        if is_break: break
        idx+=1