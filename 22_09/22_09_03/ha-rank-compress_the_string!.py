string = input()

answer = []
stack = [string[0]]
cnt = 1
for i in range(1, len(string)+1):
    if i == len(string):
        answer.append((cnt, int(stack[-1])))
        break
    if stack[-1] == string[i]:
        cnt+=1
    else:
        answer.append((cnt, int(stack[-1])))
        stack.append(string[i])
        cnt = 1
print(" ".join(list(map(str, answer))))
