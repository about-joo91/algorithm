brackets = list(input())
answer = 0
stack = []
for bracket in brackets:
	if bracket == ')':
		if stack:
			stack.pop()
		else:
			answer += 1
	else:
		stack.append('(')

print(answer + len(stack))
