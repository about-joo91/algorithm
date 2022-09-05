def solution(money):
    N = len(money)
    dp_visited_first = [0] * N  
    dp_visited_first[0] = dp_visited_first[1] = money[0]
    for i in range(2, N-1):
        dp_visited_first[i] = max(dp_visited_first[i-2] + money[i], dp_visited_first[i-1])
    
    dp_unvisited_first = [0] * N  
    dp_unvisited_first[0] = 0
    dp_unvisited_first[1] = money[1]    
    for i in range(2, N):
        dp_unvisited_first[i] = max(dp_unvisited_first[i-2] +money[i], dp_unvisited_first[i-1])
    
    return max(dp_visited_first[N-2], dp_unvisited_first[N-1])


print(solution([1,2,3,1,5]))