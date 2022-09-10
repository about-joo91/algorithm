import sys
input = sys.stdin.readline

N = int(input())
values = sorted(list(map(int, input().split())))
M = int(input())
wanted_values = list(map(int, input().split()))

for wanted_value in wanted_values:
    left = 0
    right = len(values)-1
    while left <= right:
        mid = (left + right)//2
        if values[mid] == wanted_value:
            print("1")
            break
        elif values[mid] < wanted_value:
            left = mid+1
        else:
            right = mid-1
    else:
        print("0")