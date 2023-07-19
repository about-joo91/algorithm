import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
jobs = [[] for _ in range(N + 1)]
blocking_job_counts = [0] * (N + 1)
durations = [0] * (N + 1)
answers = [0] * (N + 1)

for cur_job in range(1, N + 1):
	job_info = list(map(int, input().rstrip().split()))

	blocking_job_counts[cur_job] = job_info[1]
	durations[cur_job] = job_info[0]
	for preceding_job in job_info[2:]:
		jobs[preceding_job].append(cur_job)

working_job_queue = deque()
for job in range(1, N + 1):
	if blocking_job_counts[job] == 0:
		working_job_queue.append(job)
		answers[job] = durations[job]

while working_job_queue:
	cur_job = working_job_queue.popleft()
	for next_job in jobs[cur_job]:
		blocking_job_counts[next_job] -= 1
		answers[next_job] = max(answers[next_job],
		                        answers[cur_job] + durations[next_job])
		if blocking_job_counts[next_job] == 0:
			working_job_queue.append(next_job)

print(max(answers))
