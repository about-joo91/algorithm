N = int(input())

word_cnts = dict()
for _ in range(N):
    word = input()
    if word in word_cnts:
        word_cnts[word]+=1
    else:
        word_cnts[word] = 1
print(word_cnts.values())