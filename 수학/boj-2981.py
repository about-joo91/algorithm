N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

arr = []
for i in range(1, N):
    arr.append(numbers[i] - numbers[i-1])

cur_gcd = arr[0]
for i in range(1, len(arr)):
    cur_gcd = gcd(cur_gcd, arr[i])

result = set()
for i in range(2, int(cur_gcd ** (1/2)) +1):
    if cur_gcd % i == 0:
        result.add(i)
        result.add(cur_gcd // i)

result.add(cur_gcd)
print(*sorted(list(result)))