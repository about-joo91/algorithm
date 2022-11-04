from typing import List
import copy
import sys


def paint_blind_spot(row, col,direction, cctv_map):

    for d in direction:
        nrow, ncol = row, col
        while True:
            nrow += direction_list[d][0]
            ncol += direction_list[d][1]
            if 0 <= nrow < N and 0 <= ncol < M:
                if cctv_map[nrow][ncol] == 6:
                    break
                if cctv_map[nrow][ncol] == 0:
                    cctv_map[nrow][ncol] = "#"
            else: break
                
def get_cnt_of_blind_spot(depth: int, cctv_map: List[List[int]]) -> int:
    global answer

    if depth == len(cctvs):
        answer = min(answer , sum(map(lambda x: x.count(0), cctv_map)))
        return

    coppied_cctv_map = copy.deepcopy(cctv_map)
    row, col, cctv_type = cctvs[depth]

    for cctv_dir in cctv_direction[cctv_type]:

        paint_blind_spot(row, col, cctv_dir, coppied_cctv_map)

        get_cnt_of_blind_spot(depth+1, coppied_cctv_map)
        
        coppied_cctv_map = copy.deepcopy(cctv_map)




if __name__ == '__main__':
    sys.stdin = open('', 'r')
    N, M = map(int, input().split())
    cctv_map = [list(map(int, input().split())) for _ in range(N)]
    direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cctv_direction = [
        [],
        [[0], [1], [2], [3]], 
        [[0, 1], [2, 3]], 
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 
        [[0, 1, 2, 3]] 
    ]
    answer = int(10e9)

    cctvs = []
    for i in range(N):
        for j in range(M):
            if cctv_map[i][j] == 6:
                continue
            if cctv_map[i][j] != 0:
                cctvs.append((i,j, cctv_map[i][j]))
    get_cnt_of_blind_spot(0, cctv_map)

    print(answer)
