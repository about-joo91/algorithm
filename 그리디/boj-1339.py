import sys
input = sys.stdin.readline
N = int(input().rstrip())

alphabet_map = {}
numbers = []

for _ in range(N):
    cur_input = input().rstrip()
    numbers.append(cur_input)
    for idx, char in enumerate(cur_input):
        if char in alphabet_map:
            alphabet_map[char] += 10 ** (len(cur_input) - idx -1)
        else:
            alphabet_map[char] = 10 ** (len(cur_input) - idx -1)

sum = 0
pows = 9
for _, value in sorted(alphabet_map.items(), key=lambda x: x[1], reverse=True):
    sum += pows * value
    pows -=1

print(sum)