import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K:
            return cnt
        new_food = (first + (second*2))
        heapq.heappush(scoville, new_food)
        cnt+=1

print(solution([1, 2, 3, 9, 10, 12],7))