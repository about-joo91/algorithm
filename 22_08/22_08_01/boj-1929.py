M, N = map(int, input().split())
check_primes =[False, False] + [True] *(N-1)
primes = []
for i in range(2, N+1):
    if check_primes[i]:
        if i >= M:
            primes.append(i)
    else:
        for j in range(2*i, N+1, i):
            check_primes[j] = False

for prime in primes:
    print(prime)