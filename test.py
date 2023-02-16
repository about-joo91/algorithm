def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    
    return get_gcd(b, a % b)

A, B = map(int, input().split())
C, D = map(int, input().split())

denominator = B * D
numerator = (A * D) + (B * C)
gcd =  get_gcd(denominator, numerator)
print(numerator // gcd, end=" ")
print(denominator // gcd)