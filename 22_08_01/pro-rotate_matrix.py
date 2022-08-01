# 처음값은 [2,2,5,4] 가 주어진다고 가정하면 2,2
# 1. 다음으로 회전할 곳은 오른쪽이므로 주어진 col값인 4로 이동한다.
# 2. 4에 도착하면 아래로 내려간다. 5에 닿을때까지
# 3. 5에 닿으면 다시 column 2로 돌아가주고
# 4. 2에 닿으면 다시 2, 2로 돌아간다.
# 5. 이 회전의 과정에서 최소값을 담아 놓는다.
# 6. 스택에 미리 값을 넣어놓고 그 값과 교환하면서 회전하면 될 듯하다.
# 회전방식은 ? => r1-1, col1-1  값을 조회하여 스택에 넣는다.
# col값을 증가시킨다. col2 - 1까지
# col2 -1
# 

def solution(rows, columns, queries):
    numbers =[[0]* columns for _ in range(rows)]
    answer = []
    num = 1
    for i in range(rows):
        for j in range(columns):
            numbers[i][j] = num
            num+=1
    for query in queries:
        #2 2 5 4
        r1, c1, r2, c2 = query
        init_num = numbers[r1-1][c1-1]
        min_num = init_num
        for i in range(r1, r2):
            numbers[i-1][c1-1] = numbers[i][c1-1]
            min_num = min(min_num, numbers[i][c1-1])
        print(numbers)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))