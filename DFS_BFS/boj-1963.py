from collections import deque

N = int(input())

prime_numbers_sifter = [True] * 10001

for i in range(2, int(10000 ** 0.5) + 1):
    if prime_numbers_sifter[i]== True:
        for j in range(i*2, 10001, i):
            prime_numbers_sifter[j] = False

cnt = 0

def get_possible_prime_numbers(cur_number):
    possible_prime_numbers = []
    for i in range(4):
        for j in range(10):
            next_number = cur_number[:3-i] + str(j) + cur_number[3-i+1:]
            if int(next_number) >= 1000 and prime_numbers_sifter[int(next_number)]:
                possible_prime_numbers.append(next_number)
    return possible_prime_numbers
        
def get_least_count_to_target_password(start, end):
    queue = deque()
    queue.append((str(start), 0))
    visisted = [False] * 10000
    visisted[start] = True


    while queue:
        cur_number, count = queue.popleft()

        if cur_number == str(end):
            return count
        
        possible_prime_numbers = get_possible_prime_numbers(cur_number)

        for possible_prime_number in possible_prime_numbers:
            if visisted[int(possible_prime_number)]: continue
            visisted[int(possible_prime_number)] = True
            queue.append((possible_prime_number, count+1))
    
    return -1

for _ in range(N):
    cur_password, target_password = map(int, input().split())
    least_count = get_least_count_to_target_password(cur_password, target_password)
    if least_count == -1:
        print("Impossible")
    else:
        print(least_count)
