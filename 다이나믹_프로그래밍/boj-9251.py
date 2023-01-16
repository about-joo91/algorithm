fir_string = input()
sec_string = input()

lcs = [[0 for _ in range(len(sec_string) + 1)] for _ in range(len(fir_string) + 1)]

for i in range(1, len(fir_string)+1):
    for j in range(1, len(sec_string)+1):
        if fir_string[i-1] == sec_string[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[len(fir_string)][len(sec_string)])