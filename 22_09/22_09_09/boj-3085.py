# import sys
# input = sys.stdin.readline

N = int(input())
candies = [list(input()) for _ in range(N)]
answer = 1

def check_row_cnt():
    result = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candies[j-1][i] == candies[j][i]:
                cnt += 1
                result = max(result,cnt )
            else:
                cnt = 1
    return result

def check_column_cnt():
    result = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candies[i][j-1] == candies[i][j]:
                cnt += 1
                result = max(result,cnt )
            else:
                cnt = 1
            
    return result

def check_cnt():
    return max(check_row_cnt(), check_column_cnt())


for i in range(N):
    for j in range(N-1):
        if candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            answer = max(answer, check_cnt())
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

for i in range(N-1):
    for j in range(N):
        if candies[i][j] != candies[i+1][j]:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            answer = max(answer, check_cnt())
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(answer)