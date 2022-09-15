import sys

input = sys.stdin.readline
N = int(input())
coordinates = list(map(int, input().split()))
dup_coordinates = sorted(list(set(coordinates[:])))
answers = []

for coordinate in coordinates:
    left = 0
    right = len(dup_coordinates)-1
    while left <= right:
        mid = (left + right)//2
        if dup_coordinates[mid] <= coordinate:
            left = mid+1
        else:
            right = mid-1
    answers.append(str(right))

print(" ".join(answers))