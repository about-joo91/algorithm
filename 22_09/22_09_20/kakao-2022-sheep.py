# 바킹독님의 비트마스크 예제로 공부
# 최대 17의 깊이의 노드 양쪽을 확인함
# 왼쪽 오른쪽 하나씩만 노드를 가질 수 있어서
left = [-1] * 20
right = [-1] * 20
# 각각의 노드를 방문여부를 비트로 표현
visited = [0] * (1 << 17)
answer = 1
val = []
n = 0

def dfs(cur_state):

    global answer
#     방문했다면 다시 검사할 필요가 없음
    if visited[cur_state]: return None
    visited[cur_state] = 1
    
    node_num, wolf = 0, 0
#   info의 수에서 늑대의 마릿수를 빼주면 양의 수가 나옴
    for i in range(n):
        if cur_state & (1 << i):
            node_num += 1
            wolf += val[i]
#   늑대가 절반 이상이라면 양을 잡아먹으므로 리턴해준다.
    if 2 * wolf >= node_num: return None
    
    answer = max(answer , node_num - wolf)
    
#   지금 현재 방문한 노드들의 아래 노드를 탐색해야함
#   따라서 cur_state 의 비트를 검사해 1 즉, 포함된 곳을 확인하여
#   그 노드의 양쪽만 검사한다.
    for i in range(n):
        if not cur_state & (1 << i):
            continue
#        -1이라면 아래노드가 비어있는 것이고
#        만약 값이 있다면 그 노드를 방문하면 됨
        if left[i] != -1:
            dfs(cur_state | (1 << left[i]))
        if right[i] != -1:
            dfs(cur_state | (1 << right[i]))
        
def solution(info, edges):
    global n, val
    val = info[:]
    n = len(info)
#     왼쪽과 오른쪽 노드들을 추가해줌
    for parent, value in edges:
        if left[parent] == -1: left[parent]= value
        else: right[parent] = value
    
    dfs(1)
    return answer