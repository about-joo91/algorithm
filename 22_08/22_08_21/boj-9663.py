N = int(input())
rows = [0] * N
answer = 0
def can_set(cur):
    for i in range(cur):
        if rows[cur] == rows[i] or abs(rows[cur] - rows[i]) == cur - i:
            return False
    return True

def back_tracking(cur):
    global answer
    if cur == N:
        answer += 1
    else:
        for i in range(N):
            rows[cur] = i
            if can_set(cur):
                back_tracking(cur+1)
back_tracking(0)
print(answer)