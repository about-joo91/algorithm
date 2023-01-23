N = int(input())
square = 9

while True:
    div, mod = divmod(N, 10 ** square)
    if mod == N:
        square -=1
        continue
    cur_digits_len = (N - (10 ** square) +1) *(square+1)
    for i in range(square):
        cur_digits_len += (9 * (10 ** i) * (i+1))
    break

print(cur_digits_len)
