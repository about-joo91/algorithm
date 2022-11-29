from copy import deepcopy

N = int(input())
initial_graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def right_move(graph:list[list[int]]):
    for row in range(N):
        change_col = N-1
        for col in range(N-1, -1, -1):
            if graph[row][col]:
                cur_value = graph[row][col]
                graph[row][col] = 0

                if graph[row][change_col] == 0:
                    graph[row][change_col] = cur_value
                elif graph[row][change_col] == cur_value:
                    graph[row][change_col] *= 2
                    change_col-=1
                else:
                    change_col-=1
                    graph[row][change_col] = cur_value
    return graph

def left_move(graph:list[list[int]]):
    for row in range(N):
        change_col = 0
        for col in range(1, N):
            if graph[row][col]:
                cur_value = graph[row][col]
                graph[row][col] = 0

                if graph[row][change_col] == 0:
                    graph[row][change_col] = cur_value
                elif graph[row][change_col] == cur_value:
                    graph[row][change_col] *=2
                    change_col+=1
                else:
                    change_col+=1
                    graph[row][change_col] = cur_value

    return graph


def down_move(graph:list[list[int]]):
    for col in range(N):
        change_row = N-1
        for row in range(N-1, -1, -1):
            if graph[row][col]:
                cur_value = graph[row][col]
                graph[row][col] = 0

                if graph[change_row][col] == 0:
                    graph[change_row][col] = cur_value
                elif graph[change_row][col] == cur_value:
                    graph[change_row][col] *=2
                    change_row -=1
                else:
                    change_row-=1
                    graph[change_row][col] = cur_value
    return graph

def up_move(graph:list[list[int]]):
    for col in range(N):
        change_row = 0
        for row in range(1, N):
            if graph[row][col]:
                cur_value = graph[row][col]
                graph[row][col] = 0
                
                if graph[change_row][col] == 0:
                    graph[change_row][col] = cur_value
                elif graph[change_row][col] == cur_value:
                    graph[change_row][col] *=2
                    change_row +=1
                else:
                    change_row+=1
                    graph[change_row][col] = cur_value
    return graph

def update_biggest_block(depth:int, cur_graph:list[list[int]]) -> None:
    global answer
    if depth == 5:
        answer = max(answer , max(map(max, cur_graph)))
        return
    
    update_biggest_block(depth+1, right_move(deepcopy(cur_graph)))
    update_biggest_block(depth+1, left_move(deepcopy(cur_graph)))
    update_biggest_block(depth+1, up_move(deepcopy(cur_graph)))
    update_biggest_block(depth+1, down_move(deepcopy(cur_graph)))
    
    

update_biggest_block(0, initial_graph)              
print(answer)