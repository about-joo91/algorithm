import sys
import heapq
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/test.txt','r')

N = int(input())
START, END = 0, 1
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)])

queue = []
heapq.heappush(queue, lectures[0][END])

for i in range(1, N):
    if lectures[i][START] < queue[0]:
        heapq.heappush(queue, lectures[i][END])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lectures[i][END])

print(len(queue))