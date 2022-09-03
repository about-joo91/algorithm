import re
N = int(input())

for _ in range(N):
    phone_num = input().strip()
    if re.match(r"[7-9]\d{9}$", phone_num):
        print("YES")
    else:
        print("NO")