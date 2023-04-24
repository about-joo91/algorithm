from functools import reduce

def get_gcd(A, B):
    if A < B:
        A, B = B, A
    
    if B == 0:
        return A
    
    return get_gcd(B, A%B)

N, S = map(int, input().split())
brothers = list(map(int, input().split()))

for i in range(N):
    brothers[i] = abs(brothers[i] - S)

answer = reduce(get_gcd, brothers)
print(answer)