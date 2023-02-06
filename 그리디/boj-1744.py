N = int(input())
numbers = [int(input()) for _ in range(N)]

left = []
right = []
zero = False

for number in numbers:
    if number > 0:
        right.append(number)
    elif number == 0: zero = True
    else: left.append(number)

answer = 0
left.sort(reverse=True)
right.sort()

while len(left) > 1:
    fir = left.pop()
    sec = left.pop()
    answer += (fir * sec)
if left and not zero:
    answer += left.pop()

while len(right) > 1:
    fir = right.pop()
    sec = right.pop()
    if fir + sec > fir * sec:
        answer += (fir+sec)
    else: answer += (fir * sec)
if right:
    answer += right.pop()

print(answer)