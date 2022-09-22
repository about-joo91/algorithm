N = int(input())
M = int(input())
S = input()
left = right = answer = 0
while right < M:
    if S[right: right+3] == "IOI":
        right +=2
        if right - left == N * 2:
            answer += 1
            left += 2
    else:
        left = right = right +1
print(answer)