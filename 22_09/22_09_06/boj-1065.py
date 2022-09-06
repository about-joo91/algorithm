N = int(input())

def arithmetic_sequence(N):
    if N < 100:
        return N
    cnt = 99
    for i in range(100, N):
        hundred = i/100
        ten = (i / 10) % 10
        one = i % 10

        if (hundred - ten) == (ten - one):
            cnt+=1
    return cnt
print(arithmetic_sequence(N))