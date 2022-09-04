import heapq


def solution(jobs):
    disks = []
    answer = 0
    end, i = 0, 0
    start = -1
    
    
    def push_to_disk(start, end):
        for job in jobs:
            if start < job[0] <=end:
                heapq.heappush(disks, (job[1] , job[0]))
    
    while i < len(jobs):
        push_to_disk(start, end)
        if disks:
            cur_disk = heapq.heappop(disks)
            start = end
            end += cur_disk[0]
            answer += (end - cur_disk[1])
            i +=1
        else:
            end+=1
            
    return answer //len(jobs)