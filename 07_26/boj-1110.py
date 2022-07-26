input_num = int(input())

rights = [input_num % 10]

new_num = input_num
cnt = 1
while True:
    left = new_num // 10
    right = new_num % 10
    new_right = (left + right) % 10
    new_num = rights[-1] * 10 + new_right
    rights.append(new_right)
    if new_num == input_num:
        print(cnt)
        break
    cnt+=1