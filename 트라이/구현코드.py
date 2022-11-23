ROOT = 1 # 루트는 1로 고정
unused = 2 # 새로 정점이 추가될 때 마다 증가시킨다.
MX = 10000 * 500 + 5 # 길이가 최대 500인 문자열이 10000개 들어오는 문제라면 이렇게 둘 수 있다.
# 루트가 1부터 시작하기 때문에 여유값 5를 둔다.
check = [False] * MX
nxt = [[ ]for _ in range(MX)] # 문자열의 종류에 따라 칼럼값을 변경(현재는 알파벳 수)

def char_to_int(char):
	return ord(char) - ord('A')


def insert(string):
	global unused
	cur = ROOT
	
	for char in string:
		cur_char_int = char_to_int(char)
		for nxt_value in nxt[cur]:
			if cur_char_int in nxt_value:
				return
		nxt[cur].append((cur_char_int, unused))
		unused += 1
		cur += 1
		
	check[unused] = True
	
insert("BANANA")

print(nxt[0])
# def erase(string):
# 	global unused
	
# 	cur = ROOT
	
# 	for char in string:
# 		cur_char_int = char_to_int(char)
# 		if nxt[cur][cur_char_int] != -1:
# 			cur+=1
# 		else: break
		
# 	if cur == len(string):
		
			