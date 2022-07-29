def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == (len(triangle[i])-1):
                triangle[i][j] += triangle[i-1][j-1] 
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[len(triangle)-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# 삼각형은 대각선 양쪽 아래로만 움직인다.
# 아래로 가면서 삼각형에 있는 값들을 더해 내려간다.
