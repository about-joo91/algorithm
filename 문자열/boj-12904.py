STR = input()
target = list(input())

for _ in range(len(target)):
	if len(target) == len(STR):
		break
	char = target.pop()
	if char == 'A':
		continue
	else:
		target = target[::-1]

if STR == ''.join(target):
	print(1)
else: print(0)
