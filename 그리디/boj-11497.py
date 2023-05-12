T = int(input())
for _ in range(T):
    N = int(input())
    numbers = sorted(list(map(int, input().split())), reverse=True)
    left = [numbers[0]]
    right = [numbers[0]]
    answer = 0
    for i in range(1, N):
      if i % 2 == 0:
        cur_num = right[-1]
        right.append(numbers[i])
      else:
        cur_num = left[-1]
        left.append(numbers[i])
      
      answer = max(answer, abs(cur_num - numbers[i]))
    print(answer)
