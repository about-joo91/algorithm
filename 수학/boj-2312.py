LIMIT = 100001
check_number_limit = int(100000 ** 0.5)
prime_numbers = [True] * LIMIT
for i in range(2, check_number_limit+1):
	if not prime_numbers[i]: continue
	for j in range(i+i, LIMIT, i):
		prime_numbers[j] = False

T = int(input())
for _ in range(T):
	cur_number = int(input())
	for i in range(2, LIMIT):
		if prime_numbers[i]:
			cnt = 0
			while cur_number > 0 and cur_number % i == 0:
				cur_number //= i
				cnt+=1
			if cnt > 0: print(i, cnt)
			if cur_number == 0: break
