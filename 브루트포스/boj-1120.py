fir_word, sec_word = map(str,input().split(' '))
LIMIT = len(sec_word) - len(fir_word)
answer = int(10e9)


for i in range(LIMIT+1):
    cnt = 0
    for j in range(len(fir_word)):
        if fir_word[j] != sec_word[i+j]: cnt+=1
    answer= min(answer, cnt)

print(answer)