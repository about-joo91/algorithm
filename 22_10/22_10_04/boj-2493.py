#  처음에 접근했던 방식
import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().rstrip().split()))
send_tower = []
answers = [0] * N 
index = -1
while towers:
    cur_tower = towers.pop()
    if towers and towers[-1] > cur_tower:
        while send_tower and towers[-1] > send_tower[-1][0]:
            _, send_index = send_tower.pop()
            answers[send_index] = N+index
        answers[index] = N+index
    else:
        send_tower.append((cur_tower, index))
        send_tower.sort(reverse=True)
    index-=1
while send_tower:
    _, index = send_tower.pop()
    answers[index] = 0
print(answers)
# 시간초과 판정을 받았다. N번 리스트를 순회하면서 동시에 
# 조건을 만족하면 send_tower라는 스택에 넣고 sort를 해서 작은값들만 가져올 수 있게 만든 코드
# 전체 타워를 N이라고 하고 가상의 스택을 M이라고 한다면
# N * MlogM + M
# 다음과 같은 어어어어엄청나게 비효율적인 BigO가 나온다.

# 풀이를 보 참고한 코드
import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().rstrip().split()))
send_tower = []
answers = []
index = -1

for i in range(N):
    while send_tower:
        if send_tower[-1][1] > towers[i]:
            answers.append(send_tower[-1][0]+1)
            break
        else:
            send_tower.pop()
    if not send_tower:
        answers.append(0)
    send_tower.append([i, towers[i]])

print(" ".join(map(str,answers)))

# 개선버전
import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().rstrip().split()))
send_tower = []
answers = []
index = -1

for i in range(N):
    while send_tower:
        if send_tower[-1][1] > towers[i]:
            answers.append(send_tower[-1][0]+1)
            break
        else:
            send_tower.pop()
    if not send_tower:
        answers.append(0)
    send_tower.append([i, towers[i]])

print(" ".join(map(str,answers)))

# send타워는 비교군을 줄을 세워 비교를 진행하고
# 뒤에 세워진 타워보다 작은 값이라면 비교할 필요가 없기 때문에
# pop으로 작은값을 제거해준다.
# send타워 스택에 담긴 값들을 비교를 마치고 나면 
# 스택에 지금 타워값을 넣어준다.