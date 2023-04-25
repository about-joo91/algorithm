N = int(input())
moving_time = 1
for _ in range(N-1):
    moving_time = moving_time * 2 + 1
def hanoi(len_of_disk, start, end, between):
    if len_of_disk == 1:
        print(start, end)
    else:
        hanoi(len_of_disk-1, start, between, end)
        print(start, end)
        hanoi(len_of_disk-1, between, end, start)

print(moving_time)
if N <= 20:
    hanoi(N, 1, 3, 2)