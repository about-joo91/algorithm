import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input().rstrip())
    phone_numbers = sorted([input().rstrip() for _ in range(N)])
    for i in range(N-1):
        if phone_numbers[i+1].startswith(phone_numbers[i]):
            print("NO")
            break
    else:
        print("YES")