number_str_map = [
 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]


def number_to_str(number):
	cur_number_str = " ".join(
	 map(lambda x: number_str_map[int(x)], list(str(number))))
	return cur_number_str


N, M = map(int, input().split())
str_number_pairs = sorted([(number_to_str(i), i) for i in range(N, M + 1)],
                          key=lambda x: x[0])

for i, answer in enumerate(str_number_pairs, 1):
	print(answer[1], end=' ')
	if i % 10 == 0: print(sep='\n')
