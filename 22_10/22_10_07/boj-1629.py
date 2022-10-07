def fpow(number, square, mod):
    if square == 1:
        return number
    else:
        x = fpow(number, square//2, mod)
        if square % 2 == 0:
            return x * x % mod
        else:
            return x * x * number % mod

number, square, mod = map(int, input().split())

print(fpow(number, square) % mod)