import bisect

N = int(input())
kids = [int(input())for _ in range(N)]
LIS_of_kids = [kids[0]]

for i in range(1, N):
    if LIS_of_kids[-1] < kids[i]:
        LIS_of_kids.append(kids[i])
    else:
        idx = bisect.bisect_left(LIS_of_kids, kids[i])
        LIS_of_kids[idx] = kids[i]

print(N - len(LIS_of_kids))