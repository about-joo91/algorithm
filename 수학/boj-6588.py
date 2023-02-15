import sys
input = sys.stdin.readline
n = 1000001
erasto = [True] * n
erasto[0] = False
erasto[1] = False

sqrt = int(n ** 0.5)
for i in range(2, sqrt+1):
    if erasto[i] == True:
        for j in range(i+i, n, i):
            erasto[j] = False

while True:
    N = int(input())
    if N == 0:
        break

    for i in range(3, N):
        if erasto[i] and erasto[N-i]:
            print(f"{N} = {i} + {N-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")