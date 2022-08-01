def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)
n1, n2 = map(int, input())
if n2 > n1:
    n1, n2 = n2, n1
gcd_num = gcd(n1, n2)
print(gcd_num)
print((n1 * n2 )// gcd_num)