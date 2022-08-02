N = int(input())
results= []
def hanoi(n , cur_pos, next_pos, middle_pos):
    if n == 1:
        results.append([cur_pos, next_pos])
    else:
        hanoi(n-1, cur_pos, middle_pos, next_pos)

        results.append([cur_pos, next_pos])

        hanoi(n -1, middle_pos, next_pos, cur_pos)

hanoi(N, 1, 3, 2)
print(len(results))
for result in results:
    print(' '.join(map(str, result)))