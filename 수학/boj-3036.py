def get_gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b:
        a, b = b, a%b
    return a


N = int(input())
numbers = list(map(int, input().split()))
first = numbers[0]
others = numbers[1:]

for other in others:
    gcd = get_gcd(first, other)
    print(f"{first // gcd}/{other // gcd}")