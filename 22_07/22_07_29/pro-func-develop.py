from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        progress_now = progresses.popleft()
        speed_now = speeds.popleft()
        if (100 - progress_now) % speed_now == 0:
            cnt_now = (100 - progress_now) // speed_now
        else:
            cnt_now = (100 - progress_now) // speed_now +1
        for i in range(len(speeds)):
            speed = speeds[i]
            progresses[i] += (speed * cnt_now)
        progress_cnt = 1
        while progresses and progresses[0] >= 100:
            progress_now = progresses.popleft()
            speed_now = speeds.popleft()
            progress_cnt +=1
        answer.append(progress_cnt)
    return answer
print(solution([96,94],[3,3]))
