def is_prime_num(n):
    arr = [True] * (n + 1) 
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: 
            j = 2

            while (i * j) <= n:
                arr[i*j] = False 
                j += 1

    return arr


while True:
    N = int(input())
    if N == 0:
        break
    arr = is_prime_num(2*N)

    cnt = 0
    for i in range(N+1, (2*N )+1):
        if arr[i] == True:
            cnt+=1
    print(cnt)