from collections import deque

N, K = map(int, input().split())

numbers = deque(list(range(1, N+1)))
answers = []
while numbers:
    numbers.rotate(-(K-1))
    answers.append(str(numbers.popleft()))
print("<" + ", ".join(answers)+">")