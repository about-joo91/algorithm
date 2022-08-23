import sys
input = sys.stdin.readline
fatigue_stack, process, fatigue_less, fatigue_limit = map(int, input().split())
fatigue = 0
total_process = 0
for _ in range(24):
    if (fatigue + fatigue_stack) <= fatigue_limit:
        fatigue += fatigue_stack
        total_process += process
    else:
        fatigue = fatigue - fatigue_less if fatigue - fatigue_less > 0 else 0
print(total_process)