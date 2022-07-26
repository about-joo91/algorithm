def dfs(lotto, visited, input_nums):
    if len(lotto) == 6:
        for number in lotto:
            print(input_nums[number], end = ' ')
        print()
        return
        
    visited_now = visited[:]
    for i in range(len(visited_now)):
        if visited_now[i] ==0:
            visited_now[i] = 1
            dfs(lotto+[i], visited_now, input_nums)
            
while True:
    input_nums = list(map(int, input().split()))
    if input_nums[0] == 0:
        break
    len_of_input_nums = input_nums.pop(0)
    visited = [0] * len_of_input_nums
    dfs([],visited, input_nums)
    print()