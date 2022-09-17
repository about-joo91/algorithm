import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

name_number_map ={}
number_name_map = {}

for i in range(1, N+1):
    name = input().rstrip()
    name_number_map[name] = i
    number_name_map[i] = name

for _ in range(M):
    data = input().rstrip()
    if data.isdigit():
        print(number_name_map[int(data)])
        continue
    print(name_number_map[data])