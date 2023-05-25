import sys

_N = int(input())
crane_weights = sorted(list(map(int, input().split())), reverse=True)
_M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
count = 0
if max(boxes) >  max(crane_weights):
	print(-1)
	sys.exit(0)
while boxes:
	count += 1
	for crane_weight in crane_weights:
		for box in boxes:
			if crane_weight >= box:
				boxes.remove(box)
				break

print(count)
