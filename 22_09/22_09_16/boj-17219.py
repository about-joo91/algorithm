import sys
input = sys.stdin.readline

N, M = map(int, input().split())

password_map = {}
for _ in range(N):
    site, password = input().split()
    password_map[site] = password

for _ in range(M):
    print(password_map[input().rstrip()])