import sys

word = list(input())
word_cnt_map = {}

for char in word:
    if char in word_cnt_map:
        word_cnt_map[char] +=1
    else: word_cnt_map[char] = 1

odd_cnt = 0
mid = ""
for word, cnt in word_cnt_map.items():
    if cnt % 2 == 0: continue
    odd_cnt +=1
    mid = word
    if odd_cnt >1:
        print("I'm Sorry Hansoo")
        sys.exit(0)

answer = ""
for word, cnt in sorted(word_cnt_map.items()):
    answer += (word * (cnt //2))

print(answer + mid + answer[::-1])