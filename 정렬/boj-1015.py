N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)

answer = []
for i in range(N):
    idx = sorted_numbers.index(numbers[i])
    answer.append(idx)
    sorted_numbers[idx] = -1
print(*answer)
