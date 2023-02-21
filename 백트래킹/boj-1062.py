import sys
input = sys.stdin.readline

N, K = map(int,input().rstrip().split())

if K < 5:
    print(0)
    sys.exit(0)

MUST_KNOW = 0
for alpha in 'antic':
    order = ord(alpha) - ord('a')
    MUST_KNOW |= 1 << order

words = []
for _ in range(N):
    word = input().rstrip()
    b = 0
    for alpha in word:
        order = ord(alpha) - ord('a')
        b |= 1 << order
    words.append(b)

def get_count_readable_word(learning_word):
    read = 0
    for j in range(N):
        word = words[j]
        if (learning_word & word) == word:
            read +=1
    return read

answer = 0
def backtracking(cur_alpha, learning_word):
    global answer
    if cur_alpha > 26:
        return
    
    if bin(learning_word).count('1') == K:
        answer = max(answer, get_count_readable_word(learning_word))

    if MUST_KNOW & (1 << cur_alpha):
        backtracking(cur_alpha+1, learning_word | (1 << cur_alpha))
    else:
        backtracking(cur_alpha+1, learning_word)
        backtracking(cur_alpha+1, learning_word | (1 << cur_alpha))


backtracking(0, 0)
print(answer)
