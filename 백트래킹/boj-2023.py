def is_prime(cur_number):
    if cur_number < 2:
        return False
    for i in range(2, int(cur_number**(1/2))+1):
        if cur_number % i == 0:
            return False
    return True

def backtracking(cur_num):
    if len(cur_num) == N:
        print(cur_num)
        return
    
    for i in range(1, 10):
        next_num = cur_num + str(i)
        if is_prime(int(next_num)):
            backtracking(next_num)

N = int(input())
backtracking("")