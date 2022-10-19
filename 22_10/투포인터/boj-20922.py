
# 처음 생각한 무식한 풀이
# 시퀀스라는 리스트값을 업데이트하며 그 길이값으로 답을 찾으려고 했다.
# 이 로직은 슬라이싱을 통해서 계속 시퀀스의 값을 복사해서 업데이트 하므로 시간초과를 받았다.
length, limit = map(int, input().split())
numbers = list(map(int,input().split()))
sequence = []
answer = 0

for number in numbers:
    if sequence.count(number) < limit:
        sequence.append(number)
    else:
        answer = max(answer, len(sequence))
        sequence = sequence[sequence.index(number)+1:]
        sequence.append(number)
print(answer)

# 투포인터를 활용하여 푼 답
# 전체 length를 순회해 숫자의 갯수를 업데이트하면서
# 검사를 거치고 난 후의 포인터 값의 차이 그러니까 길이값을
# 기존의 길이값을 저장한 answer와 비교하여 더 큰값을 저장해준다.
length, limit = map(int, input().split())
numbers = list(map(int,input().split()))
left = right = 0
counts = [0] * 200001
answer = 0

while right < length:
    if counts[numbers[right]]< limit:
        counts[numbers[right]] +=1
        right +=1
    else:
        counts[numbers[left]] -=1
        left+=1
    answer = max(answer, right - left)
print(answer)