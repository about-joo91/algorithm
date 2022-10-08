import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [list(map(int, input().rstrip().split())) for _ in range(N)]

while len(numbers) !=1:
    answer_len = len(numbers)//2
    answer = [[ ] * answer_len for _ in range(answer_len)]
    for i in range(0,len(numbers),2):
        for j in range(0,len(numbers),2):
            cur_pooling = sorted([numbers[i][j], numbers[i][j+1], numbers[i+1][j+1], numbers[i+1][j]])[-2]
            answer[i//2].append(cur_pooling)
    numbers = answer
print(numbers[0][0])