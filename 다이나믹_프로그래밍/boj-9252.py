fir_str = input()
sec_str = input()

N = len(fir_str)
M = len(sec_str)

lcs = [[""] * (M+1) for _ in range(N+1)]
dp = []
max_value = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if fir_str[i-1] == sec_str[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + fir_str[i-1]
        else:
            if len(lcs[i-1][j]) > len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else: lcs[i][j] = lcs[i][j-1]

print(len(lcs[N][M]))
print("".join(lcs[N][M]))