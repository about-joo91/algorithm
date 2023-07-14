import sys
import re
input = sys.stdin.readline

def is_infected(str):
	reg = re.compile('^[A-F]?A+F+C+[A-F]?$')
	matching_str = reg.match(str)
	if matching_str:
		return True
	return False

N = int(input())
for _ in range(N):
	cur_str = input()
	if is_infected(cur_str):
		print('Infected!')
	else:
		print('Good')
