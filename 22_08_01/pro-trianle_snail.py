def solution(n):
    init_triangle_nums = [[0] * i for i in range(1,n+1)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x +=1
            elif i % 3 == 1:
                y +=1
            elif i % 3 == 2:
                x-=1
                y-=1
            init_triangle_nums[x][y] = num
            num+=1
            
    for init_triangle_num in init_triangle_nums:
        answer+= init_triangle_num
    return answer
        




print(solution(6))